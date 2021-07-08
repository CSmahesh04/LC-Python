# Optimal Solution. O(n)T, inplace
def palindrome(s):
	if len(s) == 0:  #Edge case of empty string
		return False

	left, right = 0, len(s) - 1

	while left < right: #While the pointers dont pass each other
		if not s[left].isalnum(): #check if the left pointer is pointing to a special char, if yes, then move on
			left += 1
		elif not s[right].isalnum():  #check if the right pointer is pointing to a special char, if yes, then move on
			right -= 1

		else: #in case both left and right pointer are NOT poiting to special chars,
			if s[left].lower() != s[right].lower(): #check if the chars are same. If not same then not palindrome
				return False
			else: #Else here means they are same chars. Move pointers.
				left += 1
				right -= 1

	return True


sol = palindrome('Hi, my name is MAHESH!!!')
print(sol)