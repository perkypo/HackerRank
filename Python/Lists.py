"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by  lines of commands 
where each command will be of the 7 types listed above. Iterate through 
each command in order and perform the corresponding operation on your list.
"""

arr=[]
for _ in range(int(input())):
    cmd=list(input().split())
    if(cmd[0]=='insert'):
        arr.insert(int(cmd[1]),int(cmd[2]))
    elif(cmd[0]=='print'):
        print(arr)
    elif(cmd[0]=='remove'):
        arr.remove(int(cmd[1]))
    elif(cmd[0]=='append'):
        arr.append(int(cmd[1]))
    elif(cmd[0]=='sort'):
        arr.sort()
    elif(cmd[0]=='reverse'):
        arr.reverse()
    elif(cmd[0]=='pop'):
        arr.pop(-1)
