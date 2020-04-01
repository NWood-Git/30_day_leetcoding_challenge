# Day 1 - Completed 4/1/2020
# Single Number
# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3283/

# Given a non-empty array of integers, every element appears twice except for one.
# Find that single one.
# Note: Your algorithm should have a linear runtime complexity. 
# Could you implement it without using extra memory?

# Example 1: Input: [2,2,1]
# Output: 1
# Example 2: Input: [4,1,2,1,2]
# Output: 4

def singleNumber(nums):
    nums_dict = {}
    for n in nums:
        if n in nums_dict.keys():
            del nums_dict[n]
        else:
            nums_dict[n] = 1
    for k in nums_dict.keys():
        return k

print(singleNumber([2,2,1]))
print(singleNumber([4,1,2,1,2]))

# Submission Detail:
# 16 / 16 test cases passed.
# Status: Accepted
# Runtime: 84 ms
# Memory Usage: 16.3 MB
# Your runtime beats 85.38 % of python3 submissions



def singleNumber1(nums):
    unique_nums = []
    for n in nums:
        if n not in unique_nums:
            unique_nums.append(n)
        else:
            unique_nums.remove(n)
    return unique_nums[0]

# print(singleNumber1([2,2,1]))
# print(singleNumber1([4,1,2,1,2]))

# Submission Detail 
# 16 / 16 test cases passed.
# Status: Accepted
# Runtime: 1676 ms
# Memory Usage: 16.4 MB
# Your runtime beats 9.82 % of python3 submissions.
