# Insertion Sort
# Not a good sorting algorithm
# better than bubble sort though

def insertion_sort(A):
    
    for index in range(1,len(A)):
        
        value = A[index]
        position = index
                
        while position > 0 and A[position-1] > value:
            
            A[position] = A[position - 1]
            position = position - 1
                            
        A[position] = value

def swap(A, i , j):
    A[i], A[j] = A[j], A[i]
