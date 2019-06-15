def insertion_sort(A):
    for i in range(len(A)):
        for j in range(i, len(A)):
            if A[i] > A[j]:
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
    return A
