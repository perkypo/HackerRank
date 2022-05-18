"""
You are given an integer, N. Your task is to print an alphabet rangoli of size N. 
(Rangoli is a form of Indian folk art based on creation of patterns.)
"""

import string
alphabets=string.ascii_lowercase

n=int(input())
lst=[]
if(n>0 and n<=26):
    for i in range(n-1,-1,-1):
        pattern ='-'.join(alphabets[i:n])
        print((pattern[:0:-1]+pattern[::]).center(n+3*(n-1),'-'))

    for i in range(1,n):
        pattern = '-'.join(alphabets[i:n])
        print((pattern[:0:-1]+pattern[::]).center(n+3*(n-1), '-'))
    
    print('\n')
    
    for i in range(n-1, -1, -1):
        pattern = '-'.join(alphabets[i:n])
        lst.append((pattern[:0:-1]+pattern[::]).center(n+3*(n-1), '-'))

    print('\n'.join(lst[::] + lst[-2::-1]))

