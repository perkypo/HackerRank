# Given 2 sets of integers, M and N, print their symmetric difference in ascending order. 
# The term symmetric difference indicates those values that exist in either M or N but do not exist in both.


M = int(input())
set1 = set(map(int, input().split()))
N = int(input())
set2 = set(map(int, input().split()))
l=set1.difference(set2)
l.update(set2.difference(set1))
for i in sorted(l):
    print(i)