def reverseWords(s):
    
    temp = s.split(" ")  #temp stores a list of words
    result = ""  #empty string
    for word in temp:
        word = word[::-1]   # reversing each word in the list
        result += word + " " # storing word in result and building sentence
    return result[:-1] # the slicing is important as it removes a extra whitespace at the end of the sentence.

puta= reverseWords('lets code python ok?')
print(puta)