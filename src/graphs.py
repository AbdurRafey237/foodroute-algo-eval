# shortest path algorithms for rider routing
# graph is an adjacency list: adj[u] = [(v, weight), ...]

import heapq

INF = float("inf")


# dijkstra with binary heap (heapq)
# O((V+E) log V), does not work right with negative weights
def dijkstra(adj, src):
    n = len(adj)
    dist = [INF] * n
    dist[src] = 0
    visited = [False] * n
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if visited[u]:
            continue  # old entry, skip
        visited[u] = True
        for v, w in adj[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
    return dist


# bellman ford, O(VE) worst case
# stops early if a full pass changes nothing
# works with negative weights and finds negative cycles
def bellman_ford(adj, src, return_passes=False):
    n = len(adj)
    edges = []
    for u in range(n):
        for v, w in adj[u]:
            edges.append((u, v, w))

    dist = [INF] * n
    dist[src] = 0
    passes = 0
    for _ in range(n - 1):
        passes += 1
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break

    # if we can still relax an edge there is a negative cycle
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            raise ValueError("negative cycle found")

    if return_passes:
        return dist, passes
    return dist


ALGOS = {"Dijkstra": dijkstra, "Bellman-Ford": bellman_ford}
