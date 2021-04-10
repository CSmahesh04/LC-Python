def dupes(st):

	stack = []

	for letter in st:

		if len(stack)> 0 and letter == stack[-1]:
			stack.pop()
		else:
			stack.append(letter)
	return ''.join(stack)

indices = dupes('abcddcabba')
print(indices) # cb