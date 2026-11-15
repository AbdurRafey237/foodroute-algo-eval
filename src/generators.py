# data generators for the food delivery scenario
#
# orders: (promised_delivery_time, order_id)
#   time is seconds since midnight (0 to 86399)
#
# roads: directed graph, weight = travel time in seconds
#   sparse = road grid, each junction connects to 4 neighbours (E ~ 4V)
#   dense  = hubs where most hubs have a direct route to each other (E ~ V^2/2)

import random

DAY = 86400


def make_orders(n, kind, seed=0):
    rng = random.Random(seed)
    if kind == "duplicates":
        # orders promised in 15 min slots, so only 96 different keys
        keys = [rng.randrange(96) * 900 for _ in range(n)]
    else:
        keys = [rng.randrange(DAY) for _ in range(n)]

    if kind == "sorted":
        keys.sort()
    elif kind == "reverse":
        keys.sort(reverse=True)
    elif kind == "nearly_sorted" and n > 0:
        keys.sort()
        # swap 1% of orders (late orders)
        for _ in range(max(1, n // 100)):
            i = rng.randrange(n)
            j = rng.randrange(n)
            keys[i], keys[j] = keys[j], keys[i]

    return [(k, i) for i, k in enumerate(keys)]


def make_grid(side, seed=0):
    # side x side junctions, two way roads, 30 to 600 sec per block
    # each direction has its own time (traffic is different each way)
    rng = random.Random(seed)
    n = side * side
    adj = [[] for _ in range(n)]
    for r in range(side):
        for c in range(side):
            u = r * side + c
            if c + 1 < side:
                v = u + 1
                adj[u].append((v, rng.randint(30, 600)))
                adj[v].append((u, rng.randint(30, 600)))
            if r + 1 < side:
                v = u + side
                adj[u].append((v, rng.randint(30, 600)))
                adj[v].append((u, rng.randint(30, 600)))
    return adj


def make_dense(n, p=0.5, seed=0):
    # every pair (u, v) gets a road with probability p
    # also add a ring 0->1->...->0 so every node can be reached
    rng = random.Random(seed)
    adj = [[] for _ in range(n)]
    for u in range(n):
        nxt = (u + 1) % n
        adj[u].append((nxt, rng.randint(60, 3600)))
        for v in range(n):
            if v != u and v != nxt and rng.random() < p:
                adj[u].append((v, rng.randint(60, 3600)))
    return adj


def add_bonus(adj, max_bonus, seed=0):
    # negative weights = rider bonus for passing pickup points
    # each node gets a value h[u], new weight = w + h[u] - h[v]
    # around any cycle the h values cancel out, so no negative cycles
    # but single edges can go negative
    # real distance becomes d(s,v) + h[s] - h[v], we use this to check answers
    rng = random.Random(seed)
    h = [rng.randint(0, max_bonus) for _ in range(len(adj))]
    new_adj = []
    for u in range(len(adj)):
        new_adj.append([(v, w + h[u] - h[v]) for v, w in adj[u]])
    return new_adj, h


def num_edges(adj):
    return sum(len(x) for x in adj)


def neg_fraction(adj):
    neg = 0
    for nbrs in adj:
        for _, w in nbrs:
            if w < 0:
                neg += 1
    return neg / num_edges(adj)
