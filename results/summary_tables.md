# Summary tables

## Mean time in ms (n = 10,000)

| algorithm | random | sorted | reverse | duplicates | nearly_sorted |
|---|---|---|---|---|---|
| Insertion | 1948.9 | 1.1 | 3880.4 | 1963.1 | 51.4 |
| Merge | 21.0 | 15.8 | 13.8 | 16.7 | 16.1 |
| Quick | 15.1 | 14.1 | 14.3 | 13.7 | 13.9 |
| Heap | 22.0 | 22.8 | 18.0 | 20.2 | 19.5 |
| Radix | 4.2 | 2.6 | 2.7 | 3.1 | 2.5 |

## Mean time in ms (n = 100,000)

| algorithm | random | sorted | reverse | duplicates | nearly_sorted |
|---|---|---|---|---|---|
| Merge | 318.8 | 284.7 | 234.8 | 315.4 | 268.6 |
| Quick | 293.0 | 290.6 | 229.2 | 297.0 | 216.6 |
| Heap | 369.7 | 362.1 | 341.2 | 418.1 | 361.5 |
| Radix | 72.9 | 43.3 | 55.8 | 58.2 | 54.8 |

## Growth rate (log-log slope of time vs n)

n log n gives a slope a bit above 1, n^2 gives 2, n gives 1.

| algorithm | random | sorted | reverse | duplicates | nearly_sorted |
|---|---|---|---|---|---|
| Insertion | 2.02 | 1.14 | 2.03 | 2.06 | 1.97 |
| Merge | 1.15 | 1.20 | 1.17 | 1.25 | 1.21 |
| Quick | 1.17 | 1.19 | 1.14 | 1.20 | 1.15 |
| Heap | 1.22 | 1.17 | 1.23 | 1.27 | 1.16 |
| Radix | 1.17 | 1.08 | 1.17 | 1.14 | 1.10 |

## Time / (n log2 n) in nanoseconds, random input

If the theory holds this should stay roughly flat as n grows.

| algorithm | 1000 | 5000 | 10000 | 50000 | 100000 |
|---|---|---|---|---|---|
| Merge | 149.6 | 135.7 | 158.3 | 141.6 | 192.0 |
| Quick | 112.6 | 125.7 | 113.7 | 109.0 | 176.4 |
| Heap | 127.3 | 152.7 | 165.6 | 175.4 | 222.6 |

## Peak extra memory in KB (random input)

| algorithm | 1000 | 5000 | 10000 | 50000 | 100000 |
|---|---|---|---|---|---|
| Insertion | 8 | 39 | 78 | - | - |
| Merge | 31 | 156 | 313 | 1,563 | 3,125 |
| Quick | 11 | 42 | 81 | 393 | 784 |
| Heap | 8 | 39 | 78 | 391 | 781 |
| Radix | 51 | 122 | 205 | 884 | 1,714 |

## Shortest path results (mean of 5 random sources)

| graph | weights | V | E | Dijkstra ms | Bellman-Ford ms | BF / Dijkstra | BF passes (theory max V-1) | Dijkstra wrong % | Dijkstra KB | BF KB |
|---|---|---|---|---|---|---|---|---|---|---|
| sparse | positive | 400 | 1520 | 0.35 | 2.61 | 7.5x | 17.2 (399) | 0.0 | 16 | 29 |
| sparse | negative | 400 | 1520 | 0.27 | 2.31 | 8.4x | 17.2 (399) | 43.35 | 16 | 29 |
| sparse | positive | 1600 | 6240 | 2.52 | 21.57 | 8.6x | 35 (1599) | 0.0 | 72 | 451 |
| sparse | negative | 1600 | 6240 | 1.27 | 18.51 | 14.6x | 35 (1599) | 64.2 | 72 | 451 |
| sparse | positive | 3600 | 14160 | 3.05 | 63.57 | 20.8x | 48 (3599) | 0.0 | 166 | 1,216 |
| sparse | negative | 3600 | 14160 | 2.95 | 63.66 | 21.6x | 48 (3599) | 80.22 | 166 | 1,215 |
| sparse | positive | 6400 | 25280 | 5.30 | 175.66 | 33.1x | 76.6 (6399) | 0.0 | 297 | 2,290 |
| sparse | negative | 6400 | 25280 | 5.79 | 171.82 | 29.7x | 76.6 (6399) | 72.45 | 297 | 2,289 |
| sparse | positive | 10000 | 39600 | 8.45 | 351.72 | 41.6x | 103.4 (9999) | 0.0 | 466 | 3,679 |
| sparse | negative | 10000 | 39600 | 10.24 | 343.42 | 33.5x | 103.4 (9999) | 82.14 | 466 | 3,678 |
| dense | positive | 100 | 5069 | 0.34 | 2.36 | 7.0x | 4.8 (99) | 0.0 | 10 | 257 |
| dense | negative | 100 | 5069 | 0.36 | 2.49 | 6.9x | 4.8 (99) | 37.4 | 8 | 257 |
| dense | positive | 200 | 20012 | 1.10 | 11.11 | 10.1x | 4.8 (199) | 0.0 | 28 | 1,440 |
| dense | negative | 200 | 20012 | 1.34 | 10.87 | 8.1x | 4.8 (199) | 43.9 | 23 | 1,440 |
| dense | positive | 300 | 45095 | 2.45 | 25.63 | 10.5x | 4.4 (299) | 0.0 | 44 | 3,426 |
| dense | negative | 300 | 45095 | 3.78 | 24.97 | 6.6x | 4.4 (299) | 47.33 | 39 | 3,426 |
| dense | positive | 400 | 79940 | 3.99 | 47.24 | 11.8x | 5.2 (399) | 0.0 | 64 | 6,192 |
| dense | negative | 400 | 79940 | 4.65 | 52.66 | 11.3x | 5.2 (399) | 38.65 | 60 | 6,192 |
| dense | positive | 500 | 124845 | 6.70 | 81.45 | 12.2x | 5 (499) | 0.0 | 80 | 9,651 |
| dense | negative | 500 | 124845 | 7.36 | 83.25 | 11.3x | 5 (499) | 41.28 | 81 | 9,652 |
