class Solution:
    def isValid(self, s: str) -> bool:
        
        hashmap = {")": "(", "}": "{", "]": "["}  # Closing brackets map to opening brackets
        stack=[]
        
        for char in s:  # checking brackets
            
            if char in hashmap:  #IF char is closing bracket
                
                top = stack.pop() if stack else '#'  # pop the top element in stack, if it has something.
                                                     #  If stack is empty put # in top
                if top != hashmap[char]:   #If the popped bracket is not the same as the opening bracket mapped, return false (meaning the whole string is false)
                    return False
                            
            else: # IF char is opening bracket
                stack.append(char)  # Add the opening to stack.
        
        return not stack  # Return stack would return False if stack is empty, True if stack has elements.
                          # return not stack returns True if stack is empty. This would happen if all the popped elements (top) are in hashmap[char] 

# ::: Slightly more understandable code below :::

def valid_paranthesis(s):

	stack = []
	hashmap= {")": "(", "}": "{", "]": "["}

	for char in s:

		if char not in hashmap:
			stack.append(char)

		else:

			top = stack.pop() if stack else '#'

			if top!= hashmap[char]:
				return False
	
	return not stack

print(valid_paranthesis('{()()'))
