''' 

9. PALINDROME NUMBER

Link of the Problem :- https://leetcode.com/problems/palindrome-number/

Problem Statement :- 

Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.

'''

# CODE OF THE PROBLEM

x=int(input())
if x<0:
    print(False)
else:
    y=str(x)[::-1]
    if str(x)==y:
        print(True)