"""
Given an array, arr, of N integers, calculate the respective first quartile (Q1), 
second quartile (Q2), and third quartile (Q3). It is guaranteed that Q1, Q2, and Q3 are integers.
"""

from statistics import median

N = int(input())
arr = list(map(int, input().split()))

arr.sort()

if(N%2!=0):
    Q1 = arr[:N//2]
    Q3 = arr[(N//2)+1:]
else:
    Q1 = arr[:N//2]
    Q3 = arr[N//2:]

print(int(median(Q1)))
print(int(median(arr)))
print(int(median(Q3)))