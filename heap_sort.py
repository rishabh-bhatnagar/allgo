'''
Time Complexity
Best : O(nlog(n))
Average : O(nlog(n))
Worst : O(nlog(n))
'''

def HEAP_SORT(A):

    heap_size = BUILD_MAX_HEAP(A)

    for i in range(len(A)-1, 1, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        A = MAX_HEAPIFY(A, 0, heap_size)
    return A

def BUILD_MAX_HEAP(A):

    heap_size = len(A)

    for i in range(int(len(A)/2), -1, -1):
        MAX_HEAPIFY(A, i, heap_size)
    return heap_size

def MAX_HEAPIFY(A, i, heap_size):

    l = 2 * i + 1
    r = 2 * i + 2

    #check if left side of root exists and is greater than root.
    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i

    #check if right side of root exists and is greater than root.
    if r < heap_size and A[r] > A[largest]:
        largest = r

    #change root if needed
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        MAX_HEAPIFY(A, largest, heap_size)
    return A


print(HEAP_SORT([5, 4, 3, 2, 1]))


