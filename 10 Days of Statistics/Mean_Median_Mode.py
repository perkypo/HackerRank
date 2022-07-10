"""
Given an array, X, of N integers, calculate and print the respective mean, median, and mode on separate lines. 
If your array contains more than one modal value, choose the numerically smallest one.

Note: Other than the modal value (which will always be an integer), your answers should be in decimal form, 
rounded to a scale of 1 decimal place.
"""

import numpy as np
from scipy import stats

N = int(input())
arr = list(map(int, input().split()))

print(round(np.mean(arr),1), round(np.median(arr),1), *stats.mode(arr)[0], sep = '\n')