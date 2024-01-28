#You have to take input in an array (list in the case of Python). Find the index of the
#element in the array such that the sum of all the elements left to that index is equal to
#the sum of all the elements right to that index. That is, split the array into equal sum of
#subarrays.
#Example:
#INPUT- [2, 4, 2, 0]
#OUTPUT- Index 1
#INPUT-[6,1,9,1,2,1,3]
#OUTPUT- Index 2

def split_array(arr):
	for i in range(len(arr)):
		if sum(arr[:i]) == sum(arr[i+1:]):
			return i
	return -1

arr=input("Enter the array: ").split()
arr=[int(i) for i in arr]
print('Index',split_array(arr))
