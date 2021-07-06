## THIS IS LC_1822
# Optimal solution O(N)

def product(nums):

	sign = 1 # Tracks sign of the Product

	for num in nums:
		if num < 0: #If negative number is encounterd, mulitply sign with -1
			sign = sign * (-1)
		elif num == 0: # If 0 even once then we make whole product 0
			return 0
	return sign

solution = product([1,2,3,45,-5,-7,1])
print(solution)