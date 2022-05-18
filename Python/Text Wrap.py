"""
You are given a string S and width W.
Your task is to wrap the string into a paragraph of width W.
"""

import textwrap

def wrap(string, max_width):
    # print textwrap.fill(string,max_width)
    return("\n".join(textwrap.wrap(string, max_width)))

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)

"""
S = input()
w = int(input())
print("\n".join([S[i:i+w] for i in range(0,len(S),w)]))
"""
