"""
You are given a string and your task is to swap cases. In other words, 
convert all lowercase letters to uppercase letters and vice versa.
"""

def swap_case(s):
    solution=""
    for letter in s:
        if(letter.isupper()):
            solution+=letter.lower()
        else:
            solution+=letter.upper()
    return solution

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
