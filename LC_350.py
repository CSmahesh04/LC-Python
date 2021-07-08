#Naive Solution: VERY BAD solution
#Basically a O(N^3)T and O(N)S
#.remove() is O(N) worst case
'''
def two_arrays(nums1, num2):
	arr =[]
	for i in nums1:
		for j in nums2:
			if i == j:
				arr.append(j)
				nums2.remove(j)
				break
	return arr'''


# Optimal Solution O(N)ST

def two_arrays(nums1, nums2):
	hashmap = {}
	arr = []

	for num in nums1: # Basically counting the occurences of each number in list 1
		if num in hashmap:
			hashmap[num] += 1 #hashmap has {number: occurences}
		else:
			hashmap[num] = 1

	for num in nums2: # If the number in list2 is in hashmap and greater than zero then its OK and appended.
		if num in hashmap and hashmap[num] > 0: #
			arr.append(num)
			hashmap[num] -= 1 #Very imp to decrease the occurences count or every same number will be appended.
	
	return arr

solution = two_arrays([1,2,2,2,3,4,5,6,7],[1,2,3,4,5,6,10])
print(solution)
