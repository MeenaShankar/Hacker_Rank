'''A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string s, which is the company name in lowercase letters, your task is to find the top three most common characters in the string.
Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,
GOOGLE would have it's logo with the letters G, O, E.


Input Format :
A single line of input containing the string S.

Constraints :
3 < len(S) <= 10^4

Output Format :
Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.


Sample Input :
aabbbccde

Sample Output :
b 3
a 2
c 2

Explanation :
aabbbccde
Here, b occurs 3 times. It is printed first.
Both a and c occur 2 times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.
Note: The string S has at least 3 distinct characters.'''

Solution1:
  using collection:
    
    import math
import os
import random
import re
import sys
import collections

s = sorted(input().strip())
s_counter = collections.Counter(s).most_common(5)
s_counter = sorted(s_counter, key=lambda x: (x[1]*-1,x[0]))
for i in range(0, 3):
    print(s_counter[i][0], s_counter[i][1])
    
Solution2:
 Without collections:
  def occurense(string):
    word_dict={}
    sort_key =[]
    for i in string:
        if i in sort_key:
            word_dict[i]+=1
        else:
            word_dict[i]=1
        sort_key.append(i)
    sort_key=sorted(list(set(sort_key)))
    sortDict_value={}
    sortDict_key={}
    values_sorted=sorted(word_dict.values(),reverse=True)
    #print(values_sorted)
    for i in values_sorted:
        for k in word_dict.keys():
            if(word_dict[k]==i):
                sortDict_value[k]=i
                word_dict.pop(k)
                break
    sort_value=list(sortDict_value.keys())
   # print(list(sort_value))
    for a1 in sort_key:
        sortDict_key[a1]=sortDict_value[a1]
    j=0
    #print(sortDict_key)
    for i in range(3):
        j=j+1
        s1=sort_value[i]
        s2=sort_value[j]
        if(sortDict_value[s1]!=sortDict_value[s2]):
            print(s1+" "+str(sortDict_value[s1]))
        else:
            for a1 in sort_key:
                if(sortDict_key[a1]==values_sorted[i]):
                    print(f"{a1} {values_sorted[i]}")
                    sortDict_key.pop(a1)
                    sort_key.remove(a1)
                    break
   

if __name__ == '__main__':
    s = input()
    occurense(s)
