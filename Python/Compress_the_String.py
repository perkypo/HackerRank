"""
You are given a string S. Suppose a character 'c' occurs consecutively X times in the string. 
Replace these consecutive occurrences of the character 'c' with (X,c) in the string.

Sample Input
1222311

Sample Output
(1, 1) (3, 2) (1, 3) (2, 1)

"""
from itertools import groupby

print(*[(len(list(X)),int(c)) for c,X in groupby(input())])