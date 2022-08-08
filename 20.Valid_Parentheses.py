''' 

20. VALID PARENTHESES

Link of the Problem :- https://leetcode.com/problems/valid-parentheses/

Problem Statement :- 

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

'''

# CODE OF THE PROBLEM

s=input()
d={')':'(','}':'{',']':'['}
stack=[]
if len(s)==0:
    print(False)
if s[0]==')' or s[0]=='}' or s[0]==']':
    print(False)
for i in s:
    if i=='(' or i=='{' or i=='[':
        stack.append(i)
    elif len(stack)>0 and stack[-1]==d[i]:
        stack=stack[:-1]
    else:
        print(False)
if len(stack)==0:
    print(True)
print(False)
