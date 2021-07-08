#Optimal Solution O(N)ST.
def anagram(s,t):
	counter = {} # Init counter

	if len(s) != len(t): #If lengths of two words not ewual then not an anagram
		return False

	for char in s : # Populating counter
		if char in counter:
			counter[char] += 1
		else:
			counter[char] = 1

	for char in t: # De-populating counter

		if char in counter:
			counter[char] -= 1
		else:      #If a letter in second string not in counter, then not an anagram
			return False

	for val in counter.values(): #If second loop didnt throw False, then FIRST string may have all characters of secoond and more.
		if val != 0 : #Check if the the counter is empty for occurences
			return False
	
	return True

indices = anagram('anagram','nagaram')
print(indices)


