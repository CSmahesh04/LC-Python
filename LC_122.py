#Optimal solution O(N)ST
def seller_stock(prices):
	profit = 0

	for idx in range(1,len(prices)): # basically going from first element to last element
		if prices[idx] > prices[idx-1]: # if sell value is greater than buy value,  
			profit = prices[idx] - prices[idx-1] + profit # add the difference(new profit) to already existing profit for compound value.

	return profit

solution = seller_stock([7,1,3,5,7,9,1])
print(solution)