# makes the charts in figures/ and the summary tables in results/
# python src/plots.py

import csv
import math
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(__file__)
RES = os.path.join(HERE, "..", "results")
FIG = os.path.join(HERE, "..", "figures")

COLORS = {"Insertion": "#e87ba4", "Merge": "#2a78d6", "Quick": "#eb6834",
          "Heap": "#1baf7a", "Radix": "#eda100",
          "Dijkstra": "#2a78d6", "Bellman-Ford": "#eb6834"}
MARKERS = {"Insertion": "v", "Merge": "o", "Quick": "s", "Heap": "^", "Radix": "D",
           "Dijkstra": "o", "Bellman-Ford": "s"}
KINDS = ["random", "sorted", "reverse", "duplicates", "nearly_sorted"]
SORTS = ["Insertion", "Merge", "Quick", "Heap", "Radix"]

plt.rcParams.update({
    "font.size": 10, "axes.spines.top": False, "axes.spines.right": False,
    "axes.edgecolor": "#999", "axes.labelcolor": "#333", "xtick.color": "#555",
    "ytick.color": "#555", "axes.grid": True, "grid.color": "#e6e6e6",
    "grid.linewidth": 0.7, "lines.linewidth": 2, "lines.markersize": 6,
    "figure.facecolor": "white", "savefig.dpi": 160,
})


def load(name):
    with open(os.path.join(RES, name)) as fh:
        return list(csv.DictReader(fh))


def label_end(ax, x, y, text):
    ax.annotate(text, (x, y), xytext=(5, 0), textcoords="offset points",
                va="center", fontsize=8, color="#333")


# ---------------- sorting ----------------
def sort_runtime(rows):
    fig, axes = plt.subplots(1, 5, figsize=(17, 3.8), sharey=True)
    for ax, kind in zip(axes, KINDS):
        for alg in SORTS:
            pts = sorted((int(r["n"]), float(r["mean_s"]) * 1000)
                         for r in rows if r["algorithm"] == alg and r["input"] == kind)
            if not pts:
                continue
            xs, ys = zip(*pts)
            ax.plot(xs, ys, color=COLORS[alg], marker=MARKERS[alg], label=alg)
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_title(kind.replace("_", " "), fontsize=10)
        ax.set_xlabel("number of orders (n)")
    axes[0].set_ylabel("mean time (ms, log scale)")
    axes[0].legend(frameon=False, fontsize=8, loc="upper left")
    fig.suptitle("Sorting time vs input size, by input type", x=0.01, ha="left")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, "sort_runtime.png"))
    plt.close(fig)


def sort_memory(rows):
    n = 100000
    algs = [a for a in SORTS if a != "Insertion"]
    vals = [int(next(r for r in rows if r["algorithm"] == a and r["input"] == "random"
                     and int(r["n"]) == n)["peak_mem_bytes"]) / 1024 for a in algs]
    fig, ax = plt.subplots(figsize=(6, 3.5))
    bars = ax.bar(algs, vals, color="#2a78d6", width=0.55)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v, f"{v:,.0f} KB", ha="center",
                va="bottom", fontsize=8, color="#333")
    ax.set_ylabel("peak extra memory (KB)")
    ax.set_title("Peak memory, n = 100,000 random orders", loc="left", fontsize=10)
    ax.grid(axis="x", visible=False)
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, "sort_memory.png"))
    plt.close(fig)


def slope(xs, ys):
    # slope of log(time) vs log(n), ~1 means linear, ~2 means quadratic
    return np.polyfit(np.log(xs), np.log(ys), 1)[0]


def sort_tables(rows):
    out = []
    out.append("## Mean time in ms (n = 10,000)\n")
    out.append("| algorithm | " + " | ".join(KINDS) + " |")
    out.append("|---" * (len(KINDS) + 1) + "|")
    for alg in SORTS:
        cells = []
        for k in KINDS:
            r = next(r for r in rows if r["algorithm"] == alg and r["input"] == k
                     and int(r["n"]) == 10000)
            cells.append(f"{float(r['mean_s'])*1000:.1f}")
        out.append(f"| {alg} | " + " | ".join(cells) + " |")

    out.append("\n## Mean time in ms (n = 100,000)\n")
    out.append("| algorithm | " + " | ".join(KINDS) + " |")
    out.append("|---" * (len(KINDS) + 1) + "|")
    for alg in SORTS[1:]:
        cells = []
        for k in KINDS:
            r = next(r for r in rows if r["algorithm"] == alg and r["input"] == k
                     and int(r["n"]) == 100000)
            cells.append(f"{float(r['mean_s'])*1000:.1f}")
        out.append(f"| {alg} | " + " | ".join(cells) + " |")

    out.append("\n## Growth rate (log-log slope of time vs n)\n")
    out.append("n log n gives a slope a bit above 1, n^2 gives 2, n gives 1.\n")
    out.append("| algorithm | " + " | ".join(KINDS) + " |")
    out.append("|---" * (len(KINDS) + 1) + "|")
    for alg in SORTS:
        cells = []
        for k in KINDS:
            pts = sorted((int(r["n"]), float(r["mean_s"]))
                         for r in rows if r["algorithm"] == alg and r["input"] == k)
            xs, ys = zip(*pts)
            cells.append(f"{slope(xs, ys):.2f}")
        out.append(f"| {alg} | " + " | ".join(cells) + " |")

    out.append("\n## Time / (n log2 n) in nanoseconds, random input\n")
    out.append("If the theory holds this should stay roughly flat as n grows.\n")
    sizes = sorted({int(r["n"]) for r in rows})
    out.append("| algorithm | " + " | ".join(str(s) for s in sizes) + " |")
    out.append("|---" * (len(sizes) + 1) + "|")
    for alg in ["Merge", "Quick", "Heap"]:
        cells = []
        for s in sizes:
            r = next(r for r in rows if r["algorithm"] == alg and r["input"] == "random"
                     and int(r["n"]) == s)
            cells.append(f"{float(r['mean_s'])*1e9/(s*math.log2(s)):.1f}")
        out.append(f"| {alg} | " + " | ".join(cells) + " |")

    out.append("\n## Peak extra memory in KB (random input)\n")
    out.append("| algorithm | " + " | ".join(str(s) for s in sizes) + " |")
    out.append("|---" * (len(sizes) + 1) + "|")
    for alg in SORTS:
        cells = []
        for s in sizes:
            r = [r for r in rows if r["algorithm"] == alg and r["input"] == "random"
                 and int(r["n"]) == s]
            cells.append(f"{int(r[0]['peak_mem_bytes'])/1024:,.0f}" if r else "-")
        out.append(f"| {alg} | " + " | ".join(cells) + " |")
    return "\n".join(out)


# ---------------- graphs ----------------
def graph_runtime(rows):
    fig, axes = plt.subplots(1, 2, figsize=(11, 3.8))
    for ax, g in zip(axes, ["sparse", "dense"]):
        for alg in ["Dijkstra", "Bellman-Ford"]:
            pts = sorted((int(r["E"]), float(r["mean_s"]) * 1000) for r in rows
                         if r["algorithm"] == alg and r["graph"] == g
                         and r["weights"] == "positive")
            xs, ys = zip(*pts)
            ax.plot(xs, ys, color=COLORS[alg], marker=MARKERS[alg], label=alg)
            label_end(ax, xs[-1], ys[-1], alg)
        ax.set_title(f"{g} graph ({'road grid' if g == 'sparse' else 'hub network'})",
                     loc="left", fontsize=10)
        ax.set_xlabel("number of edges (E)")
        ax.set_ylabel("mean time (ms)")
        ax.set_xlim(0, max(int(r["E"]) for r in rows if r["graph"] == g) * 1.2)
    axes[0].legend(frameon=False, fontsize=8)
    fig.suptitle("Shortest path time, non-negative weights", x=0.01, ha="left")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, "graph_runtime.png"))
    plt.close(fig)


def dijkstra_errors(rows):
    sel = [r for r in rows if r["algorithm"] == "Dijkstra" and r["weights"] == "negative"]
    labels = [f"{r['graph']}\nV={r['V']}" for r in sel]
    vals = [float(r["wrong_pct"]) for r in sel]
    fig, ax = plt.subplots(figsize=(10, 3.5))
    bars = ax.bar(range(len(vals)), vals, color="#eb6834", width=0.6)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v, f"{v:.0f}%", ha="center",
                va="bottom", fontsize=8, color="#333")
    ax.set_xticks(range(len(vals)))
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylabel("% of nodes with wrong distance")
    ax.set_ylim(0, 100)
    ax.set_title("Dijkstra on graphs with rider bonuses (negative edges). "
                 "Bellman-Ford was 0% wrong on all of these.", loc="left", fontsize=10)
    ax.grid(axis="x", visible=False)
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, "dijkstra_negative_errors.png"))
    plt.close(fig)


def graph_tables(rows):
    out = ["## Shortest path results (mean of 5 random sources)\n",
           "| graph | weights | V | E | Dijkstra ms | Bellman-Ford ms | BF / Dijkstra | "
           "BF passes (theory max V-1) | Dijkstra wrong % | Dijkstra KB | BF KB |",
           "|---|---|---|---|---|---|---|---|---|---|---|"]
    keys = []
    for r in rows:
        k = (r["graph"], r["weights"], r["V"])
        if k not in keys:
            keys.append(k)
    for g, w, v in keys:
        d = next(r for r in rows if r["algorithm"] == "Dijkstra" and
                 (r["graph"], r["weights"], r["V"]) == (g, w, v))
        b = next(r for r in rows if r["algorithm"] == "Bellman-Ford" and
                 (r["graph"], r["weights"], r["V"]) == (g, w, v))
        dt, bt = float(d["mean_s"]) * 1000, float(b["mean_s"]) * 1000
        out.append(f"| {g} | {w} | {v} | {d['E']} | {dt:.2f} | {bt:.2f} | {bt/dt:.1f}x | "
                   f"{b['bf_passes']} ({int(v)-1}) | {d['wrong_pct']} | "
                   f"{int(d['peak_mem_bytes'])/1024:,.0f} | {int(b['peak_mem_bytes'])/1024:,.0f} |")
    return "\n".join(out)


if __name__ == "__main__":
    os.makedirs(FIG, exist_ok=True)
    s = load("sort_results.csv")
    g = load("graph_results.csv")
    sort_runtime(s)
    sort_memory(s)
    graph_runtime(g)
    dijkstra_errors(g)
    with open(os.path.join(RES, "summary_tables.md"), "w") as fh:
        fh.write("# Summary tables\n\n" + sort_tables(s) + "\n\n" + graph_tables(g) + "\n")
    print("done")
