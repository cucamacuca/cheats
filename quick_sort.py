# Quick Sort
# Average O(n log n)
# Worst Case Scenario (n^2)

def quick_sort(A):

    start = 0
    end = len(A) - 1
    _quick_sort(A, start, end)

def _quick_sort(A, start, end):

    if (start < end):
        
        pivotIndex = partition(A, start, end)
        
        _quick_sort(A, start, pivotIndex -1)
        _quick_sort(A, pivotIndex + 1, end)

def partition(A, start, end):

    pivot = A[end]
    pivotIndex = start

    for x in range(start, end):
        
        if (A[x] <= pivot):
            swap(A,x, pivotIndex)
            pivotIndex = pivotIndex + 1

    swap(A, pivotIndex, end)
    return pivotIndex

def swap(A, i , j):
    A[i], A[j] = A[j], A[i]