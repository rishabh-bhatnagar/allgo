'''
Counting sort is used as a subroutine for radix sort.

Time Complexity
Best : O(k * n)
Average : O(k * n)
Worst : O(k * n)
'''

def COUNTING_SORT(A, mod): 
  
    n = len(A) 
  
    # intitalize final output array
    output = [0] * n
  
    # initialize count array as 0 
    count = [0] * 10
  
    
    for i in range(0, n): 
        index = A[i] // mod 
        count[index % 10] += 1
  
    for i in range(1,10): 
        count[i] += count[i-1] 
  
    # Build the output array 
    i = n-1
    while i>=0: 
        index = A[i] // mod 
        output[ count[index % 10] - 1] = A[i] 
        count[index % 10] -= 1
        i -= 1
  
    #copying elements from output to original array
    i = 0
    for i in range(0,len(A)): 
        A[i] = output[i] 

  

def RADIX_SORT(A): 
    max_of_list = max(A) 

    mod = 1
    while max_of_list / mod > 0: 
        COUNTING_SORT(A, mod) 
        mod *= 10
  
# Driver code to test above 
A = [1092, 79275, 254, 826, 12]
RADIX_SORT(A) 
print(A)  




