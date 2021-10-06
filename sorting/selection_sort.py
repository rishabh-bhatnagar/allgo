''' 
Time Complexity
Best: O(n^2)
Average : O(n^2)
Worst : O(n^2)
'''

def SELECTION_SORT(A):
	for i in range(len(A)):
		min_index = i

		for j in range(i + 1, len(A)):
			if A[min_index] > A[j]:
				min_index = j

		A[i], A[min_index] = A[min_index], A[i]

A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
SELECTION_SORT(A)
print(A)

