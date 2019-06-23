
def partition(A, p, r):
    pivot = A[r] # last index is pivot

    i = p - 1 # smaller element

    # goes through whole array
    for j in range(p, r):
        # if current elem is <= pivot, swap current elem with smaller element
        if A[j] <= pivot:
            i += 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp

    #swap pivot to the place that it is supposed to go
    temp = A[i + 1]
    A[i + 1] = A[r]
    A[r] = temp
    return i + 1

def quick_sort_helper(A, p, r):
    if (p < r):
        p = partition(A, p, r) # partitioning index
        quick_sort_helper(A, p, p - 1)
        quick_sort_helper(A, p + 1, r)

def quick_sort(A):
    quick_sort_helper(A, 0, len(A) - 1)
    return A

