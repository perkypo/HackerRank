"""
Given an array, arr, of n integers, calculate and print the standard deviation. Your answer should be in decimal form, 
rounded to a scale of 1 decimal place (i.e., 12.3 format). An error margin of +-0.1 will be tolerated for the standard deviation.
"""

from statistics import pstdev

n = int(input())
arr = list(map(int, input().split()))

print(round(pstdev(arr),1))