"""
Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.
"""

from collections import Counter

X  = int(input())
shoe_size = list(map(int, input().split()))
size_dict = dict(Counter(shoe_size))
total = 0
N = int(input())

for _ in range(N):
    size, price = map(int, input().split())
    
    if(size_dict[size]>0):
        total += price
        size_dict[size] -= 1
        
print(total)