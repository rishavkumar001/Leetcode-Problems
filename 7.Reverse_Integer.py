''' 

7. REVERSE INTEGER

Link of the Problem :- https://leetcode.com/problems/reverse-integer/

Problem Statement :- 

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer 
range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

'''

# CODE OF THE PROBLEM

x=int(input())
rev = int(str(abs(x))[::-1])
if rev.bit_length() < 32:
    if x<0:
        print(-rev)
    else:
        print(rev)
else:
    print(0)
