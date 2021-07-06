#Optimal Solution O(N)ST. This question solution EXACTLY SAME as TWO SUM

def duplicate(nums):

	if len(nums)<2:
		return False

	hashmap = {}
	for num in nums:
		if num in hashmap:
			return True
		else:
			hashmap[num] = 'Exists in Array'
	return False

solution = duplicate([12,3,4,5,6,7,5,5,2,4,5,6])
print(solution)

#Sub-optimal solution O(NLogN)T. This solution uses sort and then two pointer, same as two sum

def duplicate(nums):
	if len(nums) <2:
		return False

	nums.sort()
	left, right = 0, 1
	while right < len(nums):
		if nums[left] == nums[right]:
			return True
		else:
			left += 1
			right += 1
	return False

solution = duplicate([12,3,4,5,6,7,5,5,2,4,5,6])
print(solution)