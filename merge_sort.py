# Merge Sort
# O(n log n)
def merge_sort(alist):
    if len(alist)>1:
        # divide and conquer
        mid = len(alist)//2
        
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0 # left index pointer
        j=0 # right index pointer
        k=0 # base index pointer

        # aList will be sorted 
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
        # merge the left half into aList
        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
        # merge the right half into aList
        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1