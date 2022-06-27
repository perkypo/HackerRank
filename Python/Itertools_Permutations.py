"""
You are given a string S.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.
"""

from itertools import permutations

s,k = map(str, input().split())
res = []

for perm in list(permutations(s, int(k))):
    res.append(''.join(perm))

res.sort()

for perm in res:
    print(perm)