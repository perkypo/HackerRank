"""
You are given a list of N lowercase English letters. For a given integer K, you can select any K indices 
(assume 1-based indexing) with a uniform probability from the list.

Find the probability that at least one of the K indices selected will contain the letter: 'a'.
"""

from itertools import combinations

N = int(input())
l = list(map(str, input().split()))
K = int(input())

res = list(combinations(sorted(l), K))
counter = 0

for ele in res:
    if('a' in ele):
        counter +=1

print(counter/len(res))