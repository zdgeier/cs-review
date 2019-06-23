#!/usr/bin/python3

import math

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [] # 1 to n1 + 1
    R = [] # 1 to n2 + 1

    for i in range(1, n1 + 1):
        L.append(A[p + i - 1])
    for j in range(1, n2 + 1):
        R.append(A[q + j])

    L.append(math.inf)
    R.append(math.inf)

    l_i = 0
    r_i = 0

    for i in range(p, r + 1):
        if L[l_i] <= R[r_i]:
            A[i] = L[l_i]
            l_i += 1
        else:
            A[i] = R[r_i]
            r_i += 1

def merge_sort_helper(A, p, r):
    if p < r:
        q = math.floor((p + r) / 2)
        merge_sort_helper(A, p, q)
        merge_sort_helper(A, q + 1, r)
        merge(A, p, q, r)

def merge_sort(A):
    merge_sort_helper(A, 0, len(A) - 1)
    return A


