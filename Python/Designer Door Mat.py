"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be N X M. (N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
"""

#worst approach

n, m = map(int, input().split())

if(n%2!=0 and m==n*3):
    mid=1
    for i in range(n):
        if(i==n//2):
            l = (m-7)//2
            r = (m-l)
            j = 0
            while(j<m):
                if(j < l or j >= r):
                    print('-', end='')
                    j += 1
                else:
                    print('WELCOME', end='')
                    j += 7
            print('')

        elif(i<n//2):
            l = (m-mid*3)//2
            r = (m-l)
            j = 0
            while(j<m):
                if(j < l or j >= r):
                    print('-', end='')
                    j += 1
                else:
                    print('.|.', end='')
                    j += 3
            print('')
            mid += 2

        elif(i>n//2):
            mid -= 2
            l = (m-mid*3)//2
            r = (m-l)
            j = 0
            while(j < m):
                if(j < l or j >= r):
                    print('-', end='')
                    j += 1
                else:
                    print('.|.', end='')
                    j += 3
            print('')

#better approach

if(n % 2 != 0 and m == n*3):
    txt = '.|.'
    for i in range(n):
        if(i < n//2):
            print(txt.center(m, '-'))
            txt += '.|..|.'

        elif(i == n//2):
            print('WELCOME'.center(m, '-'))     

        elif(i > n//2):
            txt = txt.replace('.|..|.', '', 1)
            print(txt.center(m, '-'))
            
#best approach
if(n % 2 != 0 and m == n*3):
    for i in range(1, n, 2):
        print((str('.|.')*i).center(m, '-'))

    print('WELCOME'.center(m, '-'))

    for i in range(n-2, -1, -2):
        print((str('.|.')*i).center(m, '-'))
