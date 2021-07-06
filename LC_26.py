# Optimal Solution O(N)S. Intuitive method is best
def remove_duplicates(array):

	left = 0 #Left pointer Init
	right = left+1 # Right pointer Init
	if len(array): # For empty list edge case/ non-empty array
		while right < len(array): #While right pointer not out of bounds
			if array[left] == array[right]: 
				array.pop(left) # If same value, pop value to the left
			else:
				left += 1 #If not same value, increment both pointers
				right += 1
	else:
		return "Empty Array" #if empty array
	return array

solution = remove_duplicates([])
print(solution)

#Edge Cases: Only empty array, i could think of.