"""
The provided code stub will read in a dictionary containing key/value pairs 
of name:[marks] for a list of students. Print the average of the marks array 
for the student name provided, showing 2 places after the decimal.
"""

marks = {}
for _ in range(int(input())):
    line = input().split()
    marks[line[0]] = list(map(float, line[1:]))
print('%.2f' %(sum(marks[input()])/3))
