#The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
#Print the average of the marks array for the student name provided, showing 2 places after the decimal.
#Example
#marks key:value pairs are

#'alpha': 20, 30, 40
#'beta': [30, 50, 70]
#query_name = 'beta'

#The query name is 'beta', beta's average score s (30 + 50 + 70)/3 = 50.0.
#Input Format:
#The first line contains the integer n, the number of students' records.
#The next n lines contain the names and marks obtained by a student each value separated by a space. 
#The final line contains query_name, the name of a student to query.

#Constraints
#2<n<10
#•0< marks in] < 100
#length of marks arrays = 3

#Output Format
#Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

#Sample Input 
'''3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60'''

#Sample Output 0
#56.00

#Explanation 0
#Marks for Malika are (52, 56, 60} whose average is (52+56+60)/3=56.

#PROGRAM:
n = int(input())
student_marks = {}
keyy=[]
for _ in range(n):
  name, *line = input().split()
  scores = list(map(float, line))
  student_marks[name] = scores
  keyy.append(name)
query_name = input()
for i in range(n):
  if(query_name==keyy[i]):
    result=sum(student_marks[query_name])/3.0
print("{:.2f}".format(result))
