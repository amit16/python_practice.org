__author__ = 'Admin'

'''
Regex 1- Validating the phone number
Input Format

The first line contains an integer N followed by N lines, each containing some string.

Output Format

For every string listed, print YES if it is a valid mobile number and NO if it isn’t.

Note :- Phone Number shouldn't contain any characters
'''

import re

num = int(raw_input())
digit_list = []

for i in range(0, num):
    digit = str(raw_input())
    digit_list.append(digit)

for j in range(0, num):
    l = len(digit_list[j])
    contains_789 = re.search(r'^[7,8,9]',digit_list[j]) #Checks whther String starts with 7, 8 or 9 
    contains_alpha = bool(re.search(r'\w', digit_list[j])) #Checks whther String contains any chars or not
    print contains_alpha
    if  l == 10 and contains_789 and (contains_alpha) == False :
        print "YES"
    else:
        print "NO"
