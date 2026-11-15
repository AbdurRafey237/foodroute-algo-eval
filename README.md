# foodroute-algo-eval

DAA Assignment 2 (CS-251, NUST SEECS). Deadline: 22 Nov 2026, 11:59 pm.

We compare sorting and shortest path algorithms for a food delivery app in Lahore.

- **Sorting task:** the dispatch system sorts pending orders by promised delivery time.
  Compared: Insertion, Merge, Quick, Heap, Radix sort.
- **Graph task:** finding the cheapest route for a rider on the road network.
  Compared: Dijkstra and Bellman-Ford. Negative edges are used to model rider bonuses.

Assignment brief: [docs/assignment-brief.pdf](docs/assignment-brief.pdf)
Report draft: [report/report.md](report/report.md)

## Main findings

| Task | Pick | Main reason | Main weakness | Strongest rival |
|---|---|---|---|---|
| Sorting | Radix sort | 4 to 7x faster at 100k orders, stable | integer keys only, O(n + b) memory | Merge sort |
| Shortest path | Dijkstra | 7 to 42x faster than Bellman-Ford | wrong with negative edges (37 to 82% wrong) | Bellman-Ford |

Full tables: [results/summary_tables.md](results/summary_tables.md)

## Evaluation criteria

| Sorting | Weight | | Shortest path | Weight |
|---|---|---|---|---|
| Runtime | 35% | | Runtime | 40% |
| Fit for the data | 30% | | Correctness for our weights | 35% |
| Stability | 20% | | Memory | 15% |
| Memory | 15% | | Extra features | 10% |

Memory is weighted low because a server has plenty of RAM. On an edge device (rider phone,
counter scanner) it would get more weight.

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
report/            report draft (markdown)
docs/              assignment brief
```

## How to run

Needs Python 3.10+.

```
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # Mac / Linux
pip install -r requirements.txt

python src/tests.py
python src/bench_graph.py     # around 15 sec
python src/bench_sort.py      # around 6 to 10 min, insertion sort is the slow part
python src/plots.py
```

All data is generated with fixed seeds so results can be reproduced. Times will be
different on other machines but the patterns should be the same.

Results in this repo were run on: Intel Core i7-11800H (8 cores, 16 threads), 32 GB RAM,
Windows 11, Python 3.14.2.

## Input types

Orders: random, sorted, reverse sorted, many duplicates (15 min slots, only 96 distinct
keys), nearly sorted (1% swapped).

Graphs: sparse road grid (E about 4V) and dense hub network (E about V^2/2), each with
normal weights and with negative weights (bonuses, no negative cycles).

## Work split

| Member | Work |
|---|---|
| Affan Ahmad Basra | code, data generators, tests, benchmarks, charts |
| [Teammate] | theory (complexity tables, recurrences), criteria, analysis, report writing |

## Still to do

- [ ] Teammate: read the brief and the report draft, check the theory sections (2 and 5)
- [ ] Fill in teammate name and CMS ID in the report header and contribution table
- [ ] Edit the AI usage declaration (section 11) so it matches what we actually did
- [ ] Final read through of the whole report
- [ ] Export the report to PDF (`report/report.pdf`)
- [ ] Zip the repo (without `.venv`) and submit on LMS, one submission per group
