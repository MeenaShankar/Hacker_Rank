'''
Problem :
 
You and Fredrick are good friends. Yesterday, Fredrick received N credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!
A valid credit card from ABCD Bank has the following characteristics:  

 
► It must start with a 4, 5 or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.
 
Example :
Valid Credit Card Numbers
4253625879615786
4424424424442444
5122-2368-7954-3214
 
Invalid Credit Card Numbers
42536258796157867       #17 digits in card number → Invalid 
4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
44244x4424442444        #Contains non digit characters → Invalid
0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid


Input Format :
The first line of input contains an integer N.
The next N lines contain credit card numbers 
 
Constraints :
0 < N < 100
 
Output Format :
Print 'Valid' if the credit card number is valid. Otherwise, print 'Invalid'. Do not print the quotes.


Sample Input :
6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456
 
Sample Output :
Valid
Valid
Invalid
Valid
Invalid
Invalid
 
Explanation :
4123456789123456 : Valid
5123-4567-8912-3456 : Valid
61234-576-8912-3456 : Invalid, because the card number is not divided into equal groups of 4.
4123356789123456 : Valid
5133-3367-8912-3456 : Invalid, consecutive digits 3333 is repeating 4 times.
5123 - 4567 - 8912 - 3456 : Invalid, because space '  ' and - are used as separators.'''


SOLUTION:
N=int(input()) 
for _ in range(N):   
    credit=input()
    n=len(credit)
    list_cre=[]
    flag=True
    if(n>=16 and n<=20):
        if(credit[0]!='4' and credit[0]!='5' and credit[0]!='6'):
            flag=False
        elif '-' in credit:
            list_cre=credit.split('-')
            sen_cre=""
            l=len(list_cre)
            if(len(list_cre)==4):
                for item in list_cre:
                    sen_cre+=item
                    if(not(item.isdigit())):
                        flag=False
                        #print('1',item)
                        break
                    elif(len(item)<4 or len(item)>4):
                        flag=False
                        break
                        #print('2')
                if flag:
                    count=1
                    for i in range(0,len(sen_cre)-1):
                        if(sen_cre[i]==sen_cre[i+1]):
                            count+=1
                        else:
                            count=1
                        if(count==4):
                            flag=False
                            break
            else:
                flag=False
                #print('4')
        elif(not(credit.isdigit())):
            flag=False
        else:
            count=1
            for i in range(0,len(credit)-1):
                if(credit[i]==credit[i+1]):
                    count+=1
                else:
                    count=1
                if(count==4):
                    flag=False
                    break
        
                
    else:
        flag=False
    if flag:
        print("Valid")   
    else:
        print("Invalid")
