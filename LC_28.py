def  strstr(haystack,needle):

	if not needle: #Checks if needle is an empty string or not
		return 0

	for i in range(len(haystack)): # iterating indices in the haystack string
		if haystack[i:i+len(needle)] == needle:  #checking if the slice the size of needle is equal to needle
			return i
	return 'Not there'  # after iterating thru the whole haystack, if no needle found, then return -1

indices = strstr('hellooo','oool')
print(indices)

