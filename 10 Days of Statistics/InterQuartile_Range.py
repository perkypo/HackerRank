"""
The interquartile range of an array is the difference between its first (Q1) and third (Q3) quartiles (i.e., Q3-Q1).

Given an array, values, of n integers and an array, freqs, representing the respective frequencies of values's elements, 
construct a data set, S, where each values[i] occurs at frequency freqs[i]. Then calculate and print S's interquartile range, 
rounded to a scale of  decimal place (i.e., 12.3 format).
"""

from statistics import median

n = int(input())
values = list(map(int, input().split()))
freqs = list(map(int, input().split()))
arr=[]

for i in range(n):
    for j in range(freqs[i]):
        arr.append(values[i])

arr.sort()

len_arr = sum(freqs)

if(len_arr%2!=0):
    Q1 = arr[:len_arr//2]
    Q3 = arr[(len_arr//2)+1:]
else:
    Q1 = arr[:len_arr//2]
    Q3 = arr[len_arr//2:]

print('{0:.1f}'.format(median(Q3) - median(Q1)))