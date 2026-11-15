# sorting algorithms
# each one takes a list of (key, order_id) and returns a new sorted list
# we only compare the key so we can check stability later

import random


# insertion sort
def insertion_sort(arr):
    a = list(arr)
    for i in range(1, len(a)):
        cur = a[i]
        j = i - 1
        # strict > so equal keys stay in same order (stable)
        while j >= 0 and a[j][0] > cur[0]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = cur
    return a


# merge sort, T(n) = 2T(n/2) + n
def merge_sort(arr):
    a = list(arr)
    temp = [None] * len(a)
    merge_sort_rec(a, temp, 0, len(a))
    return a


def merge_sort_rec(a, temp, lo, hi):
    if hi - lo <= 1:
        return
    mid = (lo + hi) // 2
    merge_sort_rec(a, temp, lo, mid)
    merge_sort_rec(a, temp, mid, hi)

    i, j, k = lo, mid, lo
    while i < mid and j < hi:
        if a[i][0] <= a[j][0]:  # <= keeps it stable
            temp[k] = a[i]
            i += 1
        else:
            temp[k] = a[j]
            j += 1
        k += 1
    while i < mid:
        temp[k] = a[i]
        i += 1
        k += 1
    while j < hi:
        temp[k] = a[j]
        j += 1
        k += 1
    a[lo:hi] = temp[lo:hi]


# quick sort with random pivot and hoare partition
# random pivot -> sorted/reverse input is not the worst case anymore
# hoare partition handles lots of equal keys ok
def quick_sort(arr, seed=0):
    a = list(arr)
    rng = random.Random(seed)
    quick_sort_rec(a, 0, len(a) - 1, rng)
    return a


def quick_sort_rec(a, lo, hi, rng):
    while lo < hi:
        pivot = a[rng.randint(lo, hi)][0]
        i = lo - 1
        j = hi + 1
        while True:
            i += 1
            while a[i][0] < pivot:
                i += 1
            j -= 1
            while a[j][0] > pivot:
                j -= 1
            if i >= j:
                break
            a[i], a[j] = a[j], a[i]

        # recurse on the smaller part, loop on the bigger one
        # keeps recursion depth at log n
        if j - lo < hi - j:
            quick_sort_rec(a, lo, j, rng)
            lo = j + 1
        else:
            quick_sort_rec(a, j + 1, hi, rng)
            hi = j


# heap sort (max heap)
def heap_sort(arr):
    a = list(arr)
    n = len(a)
    # build heap
    for i in range(n // 2 - 1, -1, -1):
        sift_down(a, i, n)
    # take max out one by one
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        sift_down(a, 0, end)
    return a


def sift_down(a, i, n):
    cur = a[i]
    while True:
        child = 2 * i + 1
        if child >= n:
            break
        if child + 1 < n and a[child + 1][0] > a[child][0]:
            child += 1
        if a[child][0] <= cur[0]:
            break
        a[i] = a[child]
        i = child
    a[i] = cur


# LSD radix sort, base 256 (one byte per pass)
# each pass is a stable counting/bucket sort on one digit
# only works for non negative integer keys
def radix_sort(arr, base=256):
    a = list(arr)
    if len(a) == 0:
        return a
    max_key = max(x[0] for x in a)
    shift = 0
    while (max_key >> shift) > 0:
        buckets = [[] for _ in range(base)]
        for x in a:
            buckets[(x[0] >> shift) & (base - 1)].append(x)
        a = []
        for b in buckets:
            a.extend(b)
        shift += 8
    return a


ALGOS = {
    "Insertion": insertion_sort,
    "Merge": merge_sort,
    "Quick": quick_sort,
    "Heap": heap_sort,
    "Radix": radix_sort,
}
