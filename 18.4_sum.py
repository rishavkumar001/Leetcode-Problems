''' 

18. 4 SUM

Link of the Problem :- https://leetcode.com/problems/4sum/

Problem Statement :- 

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

'''

# CODE OF THE PROBLEM

nums=list(map(int,input().split()))
target=int(input())
nums.sort()
i = 0
L = len(nums)
res = []
while i < L-3:
    if target-nums[i] < 3*nums[i+1] or target-nums[i] > 3*nums[-1]:
            while i < L-4 and nums[i] == nums[i+1]:
                i+=1
            i+=1
            continue
    j = i+1
    while j < L-2:
        if target-nums[i]-nums[j] < 2*nums[j+1] or target-nums[i]-nums[j] > 2*nums[-1]:
            while j < L-3 and nums[j] == nums[j+1]:
                j+=1
            j+=1
            continue
        left = j+1
        right = L-1
        new_target = target-nums[i]-nums[j]
        while left<right:
            if nums[left]+nums[right] > new_target:
                right-=1
            elif nums[left]+nums[right] < new_target:
                left+=1
            else:
                res.append([nums[i],nums[j],nums[left],nums[right]])
                temp_left = nums[left]
                temp_right = nums[right]
                while(left<right and nums[left]==temp_left):
                    left+=1
                while(left<right and nums[right]==temp_right):
                    right-=1
        while j < L-3 and nums[j] == nums[j+1]:
            j+=1
        j+=1
    while i < L-4 and nums[i] == nums[i+1]:
        i+=1
    i+=1
print(res)