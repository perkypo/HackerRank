"""
You are given a set A and n other sets.
Your job is to find whether set A is a strict superset of each of the n sets.

Print True, if A is a strict superset of each of the n sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.


Input Format

The first line contains the space separated elements of set A.
The second line contains integer n, the number of other sets.
The next n lines contains the space separated elements of the other sets.
"""

A = set(map(int, input().split()))

result = True

for _ in range(int(input())):
    B = set(map(int, input().split()))
    if(len(B-A)):
        result = False

print(result)