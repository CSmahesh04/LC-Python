def kdiff_pairs(arr,k):
	# This code is divided into two parts, the counter hash and the actual solve


	hashmap ={} #the first for loop builds the counter. Keys are the unique values in the array, values are the number of occurences. 

	for num in arr:
		if num in hashmap:
			hashmap[num] += 1
		else:
			hashmap[num] = 1

	count = 0

	for key in hashmap:  #iterating thru keys of the hashmap
		if k != 0:  # k is non-zero. Means the pair is not the same number.
			if k + key in hashmap:   # if 3+k =5 in hashmap, increase count
				count += 1
		else:  # if k =0, that means the pair is the same number.
			if hashmap[key] >= 2: #checking the occurences for the key. If it only occurs once then no go. Else counts
				count += 1
	return count , hashmap
ind = kdiff_pairs([2,2,5,6,7,2],0)
print(ind)
