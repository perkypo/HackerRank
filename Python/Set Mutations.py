# You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.
# Your task is to execute those operations and print the sum of elements from set A.
# 
# Input Format
# The first line contains the number of elements in set A.
# The second line contains the space separated list of elements in set A.
# The third line contains integer N, the number of other sets.
# The next 2*N lines are divided into N parts containing two lines each.
# The first line of each part contains the space separated entries of the operation name and the length of the other set.
# The second line of each part contains space separated list of elements in the other set.

len_A = int(input())
A = set(map(int,input().split()))
N = int(input())
for _ in range(N):
    operation, len_B= input().split()
    B = set(map(int,input().split()))
    if(operation == 'intersection_update'):
        A &= B # A.intersection_update(B) or A &= B
    elif(operation == 'update'):
        A |= B # A.update(B) or A |= B
    elif(operation == 'symmetric_difference_update'):
        A ^= B # A.symmetric_difference_update(B) or A ^= B
    elif(operation == 'difference_update'):
        A -= B # A.difference_update(B) or A -= B
print(sum(A))
