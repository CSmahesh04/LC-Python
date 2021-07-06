def word_distance (word1,word2,wordlis):

	x = None   # Think of x and y as pointers. x for word1
	y = None	# y for word 2.	
	result = 1000 #Stores result, but intitialized as a infinity number
	for i in range(len(wordlis)):  #Index interate thru list of words
		
		if wordlis[i] == word1:  # if word1 is matched, update x pointer location to current index
			x = i
		elif wordlis[i] == word2: # if word2 is matched, update x pointer location to current index
			y = i
		
		if y != None and x != None: 		#This only runs if both x and y are not NONE type. If both are values this if runs.
			result = min(result,abs(y-x))	#Even after result is updated, the for loop goes thru the list. If any more repeating words
											# then x and/or y will be repeated and minimum value of new vs old 'result' will be returned
	return result

indices= word_distance('ssss','Chadalavada',['My','name','is','Mahesh','Chadalavada', 'Chadalavada', 'ssss'])

print(indices)

