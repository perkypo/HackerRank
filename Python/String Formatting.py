"""
 Given an integer n, print the following values for each integer  from  1 to n:
 Decimal
 Octal
 Hexadecimal (capitalized)
 Binary
 Function Description
 Complete the print_formatted function in the editor below. 
 print_formatted has the following parameters: 
 int number: the maximum value to print
 Prints
 The four values must be printed on a single line in the order specified 
 above for each i from 1 to number. Each value should be space-padded to 
 match the width of the binary value of number and the values should be separated by a single space.
 Input Format
 A single integer denoting n. 
"""
number=int(input())
w = number.bit_length() #padding required
for i in range(1,number+1):
    print(f"{i:{w}d} {i:{w}o} {i:{w}X} {i:{w}b}")