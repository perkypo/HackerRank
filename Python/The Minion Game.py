"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.
"""

string=input()
strlen=len(string)
vowels=['A','E','I','O','U']
kevin=stuart=0
for start in range(strlen):
    if(string[start] in vowels):
        kevin += (strlen - start)
    else:
        stuart += (strlen - start)
if(kevin>stuart):
    print('Kevin {0}'.format(kevin))
elif(stuart>kevin):
    print('Stuart {0}'.format(stuart))
else:
    print('Draw')