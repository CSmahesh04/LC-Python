def two_sum(arr, target):
	left , right = 0, len(arr)-1

	while left < right:
		curr_sum = arr[left] + arr[right]
		if curr_sum == target:
			return [left, right]

		elif curr_sum > target:
			right -= 1

		else:
			left += 1

ind = two_sum([2,3,4,5,6,7,66,9], 13)
print(ind)