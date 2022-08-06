''' 

1. TWO SUM

Link of the Problem :- https://leetcode.com/problems/two-sum/

Problem Statement :- 

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

'''

# CODE OF THE PROBLEM

nums=list(map(int,input().split()))
target=int(input())
d={}
for i in range(len(nums)):
        if target-nums[i] not in d:
            d[nums[i]]=i
        else:
            print([d[target-nums[i]],i])
            break