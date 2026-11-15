# sorting benchmark
# python src/bench_sort.py  ->  results/sort_results.csv

import csv
import os
import statistics
import time
import tracemalloc

from sorting import ALGOS
from generators import make_orders

SIZES = [1000, 5000, 10000, 50000, 100000]
KINDS = ["random", "sorted", "reverse", "duplicates", "nearly_sorted"]
INSERTION_MAX = 10000  # insertion sort is O(n^2), too slow past this in python
OUT = os.path.join(os.path.dirname(__file__), "..", "results", "sort_results.csv")


def time_it(f, data, reps):
    times = []
    for _ in range(reps):
        t = time.perf_counter()
        f(data)
        times.append(time.perf_counter() - t)
    return statistics.mean(times), statistics.median(times), statistics.stdev(times)


def peak_memory(f, data):
    # extra memory the sort uses on top of the input list
    tracemalloc.start()
    f(data)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak


def main():
    rows = []
    for n in SIZES:
        reps = 7 if n <= 10000 else 5
        for kind in KINDS:
            data = make_orders(n, kind, seed=42)
            for name, f in ALGOS.items():
                if name == "Insertion" and n > INSERTION_MAX:
                    continue
                r = 3 if name == "Insertion" else reps  # insertion is slow
                f(data)  # warm up run, not counted
                mean, med, sd = time_it(f, data, r)
                mem = peak_memory(f, data)
                rows.append([name, kind, n, r, round(mean, 6), round(med, 6), round(sd, 6), mem])
                print(f"{name:10s} {kind:14s} n={n:6d}  {mean*1000:9.2f} ms  {mem/1024:9.1f} KB")

    with open(OUT, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["algorithm", "input", "n", "reps", "mean_s", "median_s", "std_s", "peak_mem_bytes"])
        w.writerows(rows)
    print("saved", OUT)


if __name__ == "__main__":
    main()
