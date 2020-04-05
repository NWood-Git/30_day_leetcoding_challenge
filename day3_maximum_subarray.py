# Day 3 - Completed 4/3/2020
# Maximum Subarray - 53. Maximum Subarray
# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3285/
# https://leetcode.com/problems/maximum-subarray/

# Given an integer array nums, find the contiguous subarray 
# (containing at least one number) which has the largest sum and return its sum.

# Example: Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Follow up: If you have figured out the O(n) solution, try coding another 
# solution using the divide and conquer approach, which is more subtle.

def maxSubArray(nums):
    max_sum = None
    temp_sum = None
    for num in nums:
        if temp_sum is None:
            temp_sum = num
            max_sum = num
        elif temp_sum < 0 and num >= temp_sum:
            temp_sum = num
        else:
            temp_sum += num
        if temp_sum > max_sum:
            max_sum = temp_sum
    return max_sum

# Submission Detail
# 202 / 202 test cases passed.
# Status: Accepted
# Runtime: 60 ms
# Memory Usage: 14.6 MB
# Your runtime beats 94.34 % of python3 submissions.

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([1,2]))


def maxSubArray_no(nums):
    max_sum = None
    temp_sum = None
    for num in nums:
        if temp_sum is None:
            temp_sum = num
        elif temp_sum < 0 and num >= temp_sum:
            temp_sum = num
        else:
            temp_sum += num
        if max_sum is None or temp_sum > max_sum:
            max_sum = temp_sum
    return max_sum

# Submission - Detail
# 202 / 202 test cases passed.
# Status: Accepted
# Runtime: 68 ms
# Memory Usage: 14.7 MB
# Your runtime beats 58.67 % of python3 submissions.

# print(maxSubArray_no([-2,1,-3,4,-1,2,1,-5,4]))
# print(maxSubArray_no([1,2]))