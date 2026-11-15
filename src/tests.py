# correctness checks, run before benchmarks
# python src/tests.py

import random
from sorting import ALGOS as SORTS
from graphs import dijkstra, bellman_ford, INF
from generators import make_orders, make_grid, make_dense, add_bonus

STABLE = {"Insertion", "Merge", "Radix"}


def test_sorting():
    for kind in ["random", "sorted", "reverse", "duplicates", "nearly_sorted"]:
        for n in [0, 1, 2, 7, 500]:
            data = make_orders(n, kind, seed=n)
            expected = sorted(data, key=lambda x: x[0])  # python sort is stable
            for name, f in SORTS.items():
                out = f(data)
                assert [x[0] for x in out] == [x[0] for x in expected], (name, kind, n)
                if name in STABLE:
                    assert out == expected, ("not stable", name, kind, n)
    print("sorting ok")


def test_stability_demo():
    # orders with same delivery slot, order_id shows arrival order
    data = make_orders(2000, "duplicates", seed=1)
    for name, f in SORTS.items():
        out = f(data)
        stable = all(not (out[i][0] == out[i + 1][0] and out[i][1] > out[i + 1][1])
                     for i in range(len(out) - 1))
        print(f"  {name:10s} stable on this input: {stable}")


def test_graphs():
    for adj in [make_grid(15, seed=2), make_dense(60, seed=3)]:
        d1 = dijkstra(adj, 0)
        d2 = bellman_ford(adj, 0)
        assert d1 == d2

        # with bonuses: bellman ford must match the real answer
        neg_adj, h = add_bonus(adj, 400, seed=4)
        bf = bellman_ford(neg_adj, 0)
        real = [d1[v] + h[0] - h[v] for v in range(len(adj))]
        assert bf == real

    # negative cycle should be caught
    cyc = [[(1, 2)], [(2, -5)], [(0, 1)]]
    try:
        bellman_ford(cyc, 0)
        assert False
    except ValueError:
        pass
    print("graphs ok")


if __name__ == "__main__":
    test_sorting()
    test_stability_demo()
    test_graphs()
