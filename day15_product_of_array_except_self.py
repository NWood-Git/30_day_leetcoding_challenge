# Day 15 - Completed 4/15/2020
# Difficulty - Medium
# Product of Array Except Self - 238. Product of Array Except Self
# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3300/
# https://leetcode.com/problems/product-of-array-except-self/

# Given an array nums of n integers where n > 1,  return an array output such that output[i] is 
# equal to the product of all the elements of nums except nums[i].

# Example: Input:  [1,2,3,4]
# Output: [24,12,8,6]

# Constraint: It's guaranteed that the product of the elements of any prefix or 
# suffix of the array (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).

# Follow up: Could you solve it with constant space complexity?
# (The output array does not count as extra space for the purpose of space complexity analysis.)

def productExceptSelf(nums):
    nums_len = len(nums)
    left  =  nums_len * [1]
    right = nums_len * [1]

    for i in range(1, nums_len):
        left[i] = left[i-1] * nums[i-1]
        
    for i in range(nums_len - 2, -1, -1):
        right [i] = right[i+1] * nums[i+1]

    result = nums_len * [1]
    for i in range(nums_len):
        result[i] = left[i] * right[i]

    return result

# Submission Detail
# 18 / 18 test cases passed.
# Status: Accepted
# Runtime: 128 ms
# Memory Usage: 20.7 MB
# Your runtime beats 51.90 % of python3 submissions.

print(productExceptSelf([1,2,3,4]))


# Great Explanation: https://www.youtube.com/watch?v=5ZihTbQ_X6o


# Seems to work but times out in leetcode
'''
def productExceptSelf(nums):
    import numpy as np
    result = []
    for i in range(len(nums)):
        nums2 = nums.copy()
        nums2.pop(i)
        result.append(np.product(nums2))
    return result
    '''