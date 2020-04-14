# Day 13 - Completed 4/13/2020
# Difficulty Medium
# Contiguous Array - 525. Contiguous Array
# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3298/
# https://leetcode.com/problems/contiguous-array/

# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1: Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

# Example 2: Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Note: The length of the given binary array will not exceed 50,000.

def findMaxLength(nums):
    track_dict = {} 
    subarr, count = 0,0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            count -= 1
        if count == 0:
            subarr = i + 1
        if count in track_dict:
            subarr = max(subarr, i - track_dict[count])
        else:
            track_dict[count] = i
    return subarr

# Submission Detail
# 555 / 555 test cases passed.
# Status: Accepted
# Runtime: 892 ms
# Memory Usage: 18.3 MB
# Your runtime beats 90.99 % of python3 submissions.

print(findMaxLength([0,1])) # 2
print(findMaxLength([0,1,0])) # 2
print(findMaxLength([0,0,1,0,0,0,1,1])) # 6
print(findMaxLength([0,1,1])) # 2

# Referenced: https://www.youtube.com/watch?v=TSAN_SSAsos