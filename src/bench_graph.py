# shortest path benchmark
# python src/bench_graph.py  ->  results/graph_results.csv

import csv
import os
import random
import statistics
import time
import tracemalloc

from graphs import dijkstra, bellman_ford
from generators import make_grid, make_dense, add_bonus, num_edges, neg_fraction

GRID_SIDES = [20, 40, 60, 80, 100]      # V = 400 .. 10000, sparse
DENSE_SIZES = [100, 200, 300, 400, 500]  # V = 100 .. 500, dense
REPS = 5
OUT = os.path.join(os.path.dirname(__file__), "..", "results", "graph_results.csv")


def run_case(rows, graph_type, adj, weights, h=None, base=None):
    n = len(adj)
    e = num_edges(adj)
    rng = random.Random(7)
    sources = [rng.randrange(n) for _ in range(REPS)]

    for name in ["Dijkstra", "Bellman-Ford"]:
        times = []
        passes = []
        wrong = []
        for s in sources:
            t = time.perf_counter()
            if name == "Dijkstra":
                dist = dijkstra(adj, s)
            else:
                dist, p = bellman_ford(adj, s, return_passes=True)
                passes.append(p)
            times.append(time.perf_counter() - t)

            # check answer against the true distances
            if h is not None:
                true_d = base_dist(base, s, h)
            else:
                true_d = dijkstra(adj, s) if name == "Bellman-Ford" else dist
            bad = sum(1 for a, b in zip(dist, true_d) if a != b)
            wrong.append(bad / n)

        tracemalloc.start()
        if name == "Dijkstra":
            dijkstra(adj, sources[0])
        else:
            bellman_ford(adj, sources[0])
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        rows.append([name, graph_type, weights, n, e,
                     round(statistics.mean(times), 6), round(statistics.stdev(times), 6),
                     peak, round(statistics.mean(passes), 1) if passes else "",
                     round(statistics.mean(wrong) * 100, 2)])
        print(f"{name:12s} {graph_type:6s} {weights:8s} V={n:6d} E={e:7d} "
              f"{statistics.mean(times)*1000:9.2f} ms  wrong={statistics.mean(wrong)*100:5.1f}%")


def base_dist(base, s, h):
    d = dijkstra(base, s)
    return [d[v] + h[s] - h[v] for v in range(len(base))]


def main():
    rows = []
    cases = [("sparse", make_grid(side, seed=side)) for side in GRID_SIDES]
    cases += [("dense", make_dense(n, seed=n)) for n in DENSE_SIZES]

    for graph_type, adj in cases:
        run_case(rows, graph_type, adj, "positive")
        max_w = max(w for nbrs in adj for _, w in nbrs)
        neg_adj, h = add_bonus(adj, max_w, seed=1)
        print(f"   negative edges: {neg_fraction(neg_adj)*100:.1f}%")
        run_case(rows, graph_type, neg_adj, "negative", h=h, base=adj)

    with open(OUT, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["algorithm", "graph", "weights", "V", "E", "mean_s", "std_s",
                    "peak_mem_bytes", "bf_passes", "wrong_pct"])
        w.writerows(rows)
    print("saved", OUT)


if __name__ == "__main__":
    main()
