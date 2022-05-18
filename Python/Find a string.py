"""
In this challenge, the user enters a string and a substring. 
You have to print the number of times that the substring occurs in the 
given string. String traversal will take place from left to right, 
not from right to left.

NOTE: String letters are case-sensitive.
"""

string=input()
substr=input()
len_substr=len(substr)
count=0

for i in range(len(string)-len_substr+1):
    if(string[i:len_substr+i]==substr):
        count=count+1

print(count)
