#Very bad method O(N) ST
# Naive method

def move_zeroes(nums):
	arr2=[] # Create an empty list
	
	for num in nums:
		if num != 0:
			arr2.append(num) # Append all non-zero nums to new list
	

	for i in range(len(nums)-len(arr2)): 
		arr2.append(0) # Append the length of the difference of lists as zero to new lists
	return arr2

ind= move_zeroes([1,0,3,0,4,5])
print(ind)


#Optimal Solution, O(N) T, O(1) S

def move_zeros(nums):
	pos = 0 #Shows position of ZEROs

	for idx in range(len(nums)):
		if nums[idx] != 0: # When a non-zero comes, idx SHOULD be in front of pos. or same as pos.
			nums[idx], nums[pos] = nums[pos], nums[idx] # We swap 0 with non-zero and vice versa. 
			pos += 1 # We increment so pos always on zero

	return nums

solution = move_zeros([0,5,0,0,4,5,5,6,7])
print(solution)