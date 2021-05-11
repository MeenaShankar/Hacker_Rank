'''
Problem Statement:
There is a horizontal row of ncubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if cubs[i] is on top of cube[j] then sidelength[j]>=sidelength[i].

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print Yes if it is possible to stack the cubes. Otherwise, print No.

Example
blocks=[1,2,3,8,7]
Result: No
After choosing the rightmost element,7, choose the leftmost element, 1. After than, the choices are 2 and 8. These are both larger than the top block of size 1.

blocks=[1,2,3,7,8]
Result: Yes

Choose blocks from right to left in order to successfully stack the blocks.

INPUT FORMAT:
The first line contains a single integer T, the number of test cases.
For each test case, there are 2 lines.
The first line of each test case contains n, the number of cubes.
The second line contains n space separated integers, denoting the sideLengths of each cube in that order.

Constraints :
1 <= T <= 5
1 <= n <= 10^5
1 <= sideLength <= 2^31

Output Format :
For each test case, output a single line containing either "Yes" or "No" without the quotes.

Sample Input :
2
6
4 3 2 1 3 4
3
1 3 2

Sample Output :
Yes
No

Explanation :
In the first test case, pick in this order: left -4 , right -4 , left -3 , right - 3, left - 2, right - 1.
In the second test case, no order gives an appropriate arrangement of vertical cubes. 3 will always come after either 1 or 2.'''
code:
from collections import deque
T=int(input())
for _ in range(T):
    n=int(input())
    flag=True
    d=deque(map(int,input().strip().split()))
    if(d[0]>=d[-1]):
        max=d.popleft()
    else:
        max=d.pop()
    while d:
        if len(d)==1:
            if d[0]>max:
                flag=False
                break
            else:
                break
        else:
            if(d[0]<=max and d[-1]<=max):
                if(d[0]>=d[-1]):
                    max=d.popleft()
                else:
                    max=d.pop()
            else:
                flag=False
                break
    if flag:
        print("Yes")
    else:
        print("No")

