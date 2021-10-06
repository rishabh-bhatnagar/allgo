'''
Comb Sort is mainly an improvement over Bubble Sort. Bubble sort always compares adjacent values. 
So all inversions are removed one by one. 
Comb Sort improves on Bubble Sort by using gap of size more than 1. 
The gap starts with a large value and shrinks by a factor of 1.3 in every iteration until it reaches the value 1. 
Thus Comb Sort removes more than one inversion counts with one swap and performs better than Bublle Sort.

The shrink factor has been empirically found to be 1.3 (by testing Combsort on over 200,000 random lists) 

Time Complexity
Best : O(n)
Average : Ω(n^2/2^p)   p denotes the number of increments and not gaps
Worst : O(n^2)
'''

def COMB_SORT(A):
	n = len(A)
	SHRINK_FACTOR = 1.3
	#initialize the gap to length of array
	gap = n

	swapped = True

	while gap > 1 or swapped:
		#finding next gap
		gap = int(float(gap) / SHRINK_FACTOR)

		swapped = False

		for i in range(0, n - gap):
			if A[i] > A[i + gap]:
				A[i], A[i + gap] = A[i + gap], A[i]
				swapped = True

A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
COMB_SORT(A)
print(A)
