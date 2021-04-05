'''
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

.Mat size must be N X M. ( Nis an odd natural number, and M is 3 times .)
.The design should have 'WELCOME' written in the center.
.The design pattern should only use |, . and - characters.

Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
Sample Input
   9 27
Sample Output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
'''
PROGRAM
n,m=map(int,input().split())
width=m
k=int((n-1)/2)
for a in range(1,k+1):
    i=a*2-1
    print((i*'.|.').center(width,'-'))
print('WELCOME'.center(width,'-'))
for a in range(k,0,-1):
    i=a*2-1
    print((i*'.|.').center(width,'-'))
