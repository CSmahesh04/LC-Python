def max_subarray(nums):

	max_sub = nums[0]
	curr_sub= 0

	for num in nums:
		if num<0:
			curr_sub=0
		curr_sub += num
		max_sub= max(max_sub,curr_sub)
	return max_sub