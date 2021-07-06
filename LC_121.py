#Optimal Solution O(N)ST. naive method would be two for loops with O(N^2)T
def stock_seller(prices):
	maxProfit = 0
	left, right = 0, 1 #Pointers Init

	while right < len(prices): # While right pointer is in bounds
		if prices[right] > prices[left]: # When sell price is higher than buy price
			profit = prices[right] - prices[left] #Make profit
			maxProfit = max(profit, maxProfit) # keep track of higherst yet profit
			right += 1 #Check out new sell price to see if lower, possibly
		else: # If sell price is higher or equal. This way Maxprofit keeps track of profit yet and buy price is lower or equal to current buy price,
				# we can check against succeeding sell prices for better profits.
			left = right # Buy price will be that price
			right += 1
	return maxProfit

solution=stock_seller([2,1,2,1,0,2,3])
print(solution)


# No edge cases, as Q says there will be vals in array.