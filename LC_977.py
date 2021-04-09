# Intuitive way 
# Time Complexity O(N LogN)

class Solution:
    def sorted_squares(self, nums: List[int]) -> List[int]:
        finArray=list(map(lambda x: x**2, nums))
        finArray.sort()
        return finArray



# Optimized Solution
# Time Complexity O(N)

class Solution:
    def sorted_squares(self, nums: List[int]) -> List[int]:

    	# nums = [-9,-8,0,1,4,7]

    	output=[]
    	length =len(nums)
    	right_index = 0

    	# length=6, right_index= 0

    	while (sums[right_index]<0 and right_index<length ):
    		right_index += 1

    		#While loop keeps iterating and increasing right_index until it is equal to 2

    	left_index = right_index - 1

    	#left_index at 1

    	#Now to write the comparator logic

    	while (left_index>=0 and right_index< length):
    		left_square= array[left_index]**2
    		right_square= array[right_index]**2

    		# While the pointer are not out of bounds, do the cpmparision and appending.
    		if left_square> right_square:
    			output.append(right_square)
    			right_index += 1

    		else:
    			output.append(left_square)
    			left_index -= 1

    	while (left_index>=0):
    		output.append(array[left_index]**2)
    		left_index -= 1
    		#once the right_index is out of bounds, we need to append all left_index values, so while left_index>=0

    	while (right_index<=length):
    		output.append(array[right_index]**2)
    		right_index += 1

    	return output







