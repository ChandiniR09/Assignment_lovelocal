#Given a string s consisting of words and spaces, return the length of the last word in the string.

s=input('Enter the string:')        #Take string as input
l=s.split()             #Obtain list of words in the string by splitting it
i=len(l)                #Number of words in the list
print('Length of the last word in the string is ',len(l[i-1]))          #Length of last word