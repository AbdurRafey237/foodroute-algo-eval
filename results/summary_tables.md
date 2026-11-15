# Summary tables

## Mean time in ms (n = 10,000)

| algorithm | random | sorted | reverse | duplicates | nearly_sorted |
|---|---|---|---|---|---|
| Insertion | 2388.4 | 1.2 | 4729.4 | 2198.2 | 55.2 |
| Merge | 32.7 | 13.8 | 14.4 | 16.4 | 15.5 |
| Quick | 17.8 | 12.4 | 19.2 | 13.8 | 16.1 |
| Heap | 23.3 | 24.7 | 21.9 | 21.9 | 19.6 |
| Radix | 4.0 | 4.0 | 3.1 | 2.2 | 2.0 |

## Mean time in ms (n = 100,000)

| algorithm | random | sorted | reverse | duplicates | nearly_sorted |
|---|---|---|---|---|---|
| Merge | 302.5 | 214.6 | 206.0 | 243.5 | 259.7 |
| Quick | 294.3 | 204.4 | 176.0 | 203.1 | 198.0 |
| Heap | 437.9 | 305.8 | 315.2 | 312.1 | 286.6 |
| Radix | 36.4 | 45.2 | 39.8 | 25.6 | 35.3 |

## Growth rate (log-log slope of time vs n)

n log n gives a slope a bit above 1, n^2 gives 2, n gives 1.

| algorithm | random | sorted | reverse | duplicates | nearly_sorted |
|---|---|---|---|---|---|
| Insertion | 2.28 | 1.22 | 2.08 | 2.06 | 1.92 |
| Merge | 1.20 | 1.16 | 1.12 | 1.13 | 1.19 |
| Quick | 1.15 | 1.09 | 1.00 | 1.12 | 1.10 |
| Heap | 1.26 | 1.14 | 1.18 | 1.19 | 1.18 |
| Radix | 1.09 | 1.12 | 1.06 | 1.03 | 1.07 |

## Time / (n log2 n) in nanoseconds, random input

If the theory holds this should stay roughly flat as n grows.

| algorithm | 1000 | 5000 | 10000 | 50000 | 100000 |
|---|---|---|---|---|---|
| Merge | 114.7 | 141.6 | 246.0 | 169.8 | 182.1 |
| Quick | 133.9 | 144.2 | 134.1 | 132.5 | 177.2 |
| Heap | 133.8 | 162.2 | 175.3 | 241.8 | 263.6 |

## Peak extra memory in KB (random input)

| algorithm | 1000 | 5000 | 10000 | 50000 | 100000 |
|---|---|---|---|---|---|
| Insertion | 8 | 39 | 78 | - | - |
| Merge | 31 | 156 | 313 | 1,563 | 3,125 |
| Quick | 11 | 43 | 82 | 395 | 785 |
| Heap | 8 | 39 | 78 | 391 | 781 |
| Radix | 52 | 122 | 205 | 884 | 1,714 |

## Shortest path results (mean of 5 random sources)

| graph | weights | V | E | Dijkstra ms | Bellman-Ford ms | BF / Dijkstra | BF passes (theory max V-1) | Dijkstra wrong % | Dijkstra KB | BF KB |
|---|---|---|---|---|---|---|---|---|---|---|
| sparse | positive | 400 | 1520 | 0.23 | 1.82 | 8.1x | 17.2 (399) | 0.0 | 19 | 33 |
| sparse | negative | 400 | 1520 | 0.31 | 1.72 | 5.5x | 17.2 (399) | 43.35 | 19 | 33 |
| sparse | positive | 1600 | 6240 | 1.09 | 15.78 | 14.5x | 35 (1599) | 0.0 | 75 | 421 |
| sparse | negative | 1600 | 6240 | 1.66 | 15.61 | 9.4x | 35 (1599) | 64.2 | 76 | 421 |
| sparse | positive | 3600 | 14160 | 5.08 | 49.64 | 9.8x | 48 (3599) | 0.0 | 169 | 1,124 |
| sparse | negative | 3600 | 14160 | 2.93 | 47.08 | 16.1x | 48 (3599) | 80.22 | 169 | 1,124 |
| sparse | positive | 6400 | 25280 | 6.71 | 120.73 | 18.0x | 76.6 (6399) | 0.0 | 300 | 2,111 |
| sparse | negative | 6400 | 25280 | 6.06 | 120.01 | 19.8x | 76.6 (6399) | 72.45 | 300 | 2,111 |
| sparse | positive | 10000 | 39600 | 7.61 | 250.23 | 32.9x | 103.4 (9999) | 0.0 | 469 | 3,388 |
| sparse | negative | 10000 | 39600 | 9.72 | 245.01 | 25.2x | 103.4 (9999) | 82.14 | 469 | 3,388 |
| dense | positive | 100 | 5069 | 0.23 | 1.49 | 6.4x | 4.8 (99) | 0.0 | 13 | 237 |
| dense | negative | 100 | 5069 | 0.22 | 1.53 | 6.9x | 4.8 (99) | 37.4 | 11 | 237 |
| dense | positive | 200 | 20012 | 0.75 | 6.00 | 8.0x | 4.8 (199) | 0.0 | 31 | 1,302 |
| dense | negative | 200 | 20012 | 0.88 | 6.38 | 7.2x | 4.8 (199) | 43.9 | 26 | 1,302 |
| dense | positive | 300 | 45095 | 1.89 | 15.21 | 8.1x | 4.4 (299) | 0.0 | 48 | 3,092 |
| dense | negative | 300 | 45095 | 3.68 | 17.16 | 4.7x | 4.4 (299) | 47.33 | 43 | 3,092 |
| dense | positive | 400 | 79940 | 3.97 | 35.66 | 9.0x | 5.2 (399) | 0.0 | 67 | 5,586 |
| dense | negative | 400 | 79940 | 4.03 | 35.47 | 8.8x | 5.2 (399) | 38.65 | 63 | 5,587 |
| dense | positive | 500 | 124845 | 5.91 | 55.92 | 9.5x | 5 (499) | 0.0 | 83 | 8,694 |
| dense | negative | 500 | 124845 | 6.21 | 58.05 | 9.3x | 5 (499) | 41.28 | 84 | 8,695 |
