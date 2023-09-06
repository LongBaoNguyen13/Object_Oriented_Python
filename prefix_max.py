def prefix_max(A, i):
    '''Return index of maximum in A[:i + 1]'''
    if i > 0:
        j = prefix(A, i - 1)
        if A[i] < A[j]:
            return j
    return i