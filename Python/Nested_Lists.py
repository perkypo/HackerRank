"""
Given the names and grades for each student in a class of n students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, 
order their names alphabetically and print each name on a new line.
"""

n=int(input())
marksheet = [[input(), float(input())] for _ in range(n)]
second_lowest=sorted(list(set(marksheet)))[1]

#print('\n'.join(a for a,b in sorted(marksheet) if b==second_lowest) )

for a,b in sorted(marksheet):
    if(b==second_lowest):
        print(a)
