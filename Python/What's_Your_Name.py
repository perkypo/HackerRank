"""
Complete the print_full_name function in the editor below.

print_full_name has the following parameters:

string first: the first name
string last: the last name
"""

def print_full_name(a, b):
    print("Hello "+ a +" " + b + "! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
