# foodroute-algo-eval

DAA Assignment 2 (CS-251, NUST SEECS)

We compare sorting and shortest path algorithms for a food delivery app in Lahore.

- **Sorting task:** the dispatch system sorts pending orders by promised delivery time.
  Compared: Insertion, Merge, Quick, Heap, Radix sort.
- **Graph task:** finding the cheapest route for a rider on the road network.
  Compared: Dijkstra and Bellman-Ford. Negative edges are used to model rider bonuses.

## Folder layout

```
src/
  sorting.py       sorting algorithms
  graphs.py        dijkstra and bellman-ford
  generators.py    order data and road graph generators
  tests.py         correctness checks
  bench_sort.py    sorting benchmark -> results/sort_results.csv
  bench_graph.py   graph benchmark   -> results/graph_results.csv
  plots.py         charts -> figures/, tables -> results/summary_tables.md
results/           raw csv results and summary tables
figures/           charts used in the report
report/            final report
```

## How to run

Needs Python 3.10+.

```
pip install -r requirements.txt
python src/tests.py
python src/bench_graph.py     # around 15 sec
python src/bench_sort.py      # around 6 to 8 min, insertion sort is the slow part
python src/plots.py
```

All data is generated with fixed seeds so results can be reproduced. Times will be
different on other machines but the patterns should be the same.

## Input types

Orders: random, sorted, reverse sorted, many duplicates (15 min slots, only 96 distinct
keys), nearly sorted (1% swapped).

Graphs: sparse road grid (E about 4V) and dense hub network (E about V^2/2), each with
normal weights and with negative weights (bonuses, no negative cycles).
