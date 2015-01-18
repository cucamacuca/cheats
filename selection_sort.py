# Selection Sort
# Variant of insertion sort
# Time complexity is worse than insertion sort
# Memory is better

def selection_sort(A):
    for i in range(len(A)):
        least = i
        for k in range( i + 1 , len(A)):
            if A[k] < A[least]:
                # get the minimum of array
                least = k
        #swap the minimum to the i
        swap( A, least, i )

def swap(A, i , j):
    A[i], A[j] = A[j], A[i]
