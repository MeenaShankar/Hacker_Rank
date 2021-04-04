#You are given a spreadsheet that contains a list of N athletes and their details (such as age, height, weight and so on).
#You are required to sort the data based on the Kth attribute and print the final resulting table. Follow the example given below for better understanding.
#Rank Age  Height(in cm)                 Rank Age  Height(in cm)
'''
1     32   190                           5     24   176
2     35   175                           4     26   195
3     41   188       sort based on k=1   1     32   190
4     26   195        i.e (age)          2     35   175
5     24   176                           3     41   188'''
#Note that K is indexed from 0 to M-1 , where M is the number of attributes.
#Note: If two attributes are the same for different rows, for example, if two atheletes are of the same age, print the row that appeared first in the input.
#Input Format
'''The first line contains N and M separated by a space.
The next N lines each contain M elements.
The last line contains K.'''

#sample input
'''5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1'''
#sample output
'''
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12'''
#PROGRAM
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    temp=[]
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i][k]>arr[j][k]):
                temp=arr[j]
                for z in range(j,i,-1):
                    arr[z]=arr[z-1]
                arr[i]=temp
    for i in range(n):
        for j in range(m):
          print(str(arr[i][j]),end=" ")
        print("")
