'''
Given a non-empty string like "Code" return a string like "CCoCodCode". 

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
'''


def string_splosion(str):
	newstr = ""
	for i in range(len(str)):
		newstr += str[:i+1]
	return newstr
		
print(string_splosion('abcde'))