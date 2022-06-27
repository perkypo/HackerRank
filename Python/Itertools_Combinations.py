"""
You are given a string S.
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.
"""

from itertools import combinations

S,k = map(str, input().split())

result = []

for i in range(1, int(k)+1):
    for j in list(combinations(sorted(S),i)):
        result.append(''.join(j))

print('\n'.join(result))