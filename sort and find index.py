### Given an array arr[] of integers of size N and a target value val. Your task is to find the indices of val in the array after sorting array in increasing order.

"""Note: The indices must be in increasing order.
* Input: arr = [1, 2, 5, 2, 3], val = 2
* Output: 1 2
* Explanation: After sorting, arr[] becomes [1, 2, 2, 3, 5]. The indices where arr[i] = 2 are 1 and 2. As the indices should be in increasing order, that’s why they are   (1, 2) and not (2, 1)
"""
arr = []
N = int(input("Number of elements"))
val = int(input("Value"))
for a in range(N):
  b=int(input())
  arr.append(b)
print(arr)
arr.sort()
print("Sorted List:",arr)
res_list = [i for i in range(N) if arr[i] == val]
listToStr = ' '.join([str(N) for N in res_list])  
print("Indices:",listToStr) 