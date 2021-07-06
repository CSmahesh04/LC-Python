# Optimal Solution O(N) ST 

def two_sum(nums, targetSum):

	hashmap = {} #Hashmap Init

	for idx in range(len(nums)): #iterating thru IDs of array
		if targetSum - nums[idx] in  hashmap: # If number in hashmap, then number exists in array too 
			return [idx,hashmap[targetSum - nums[idx]]] #Return Answer
		else:
			hashmap[nums[idx]] = idx # If number not in hashmap, add it to hasmap as {num:id}
	return False
	print(hashmap)

two= two_sum([1,2,34,55,3,4,5,6,], 89 )

print(two)