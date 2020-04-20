# Day -19: Completed 4/19/2020
# Difficulty - Medium
# Search in Rotated Sorted Array - 33. Search in Rotated Sorted Array
# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3304/
# https://leetcode.com/problems/search-in-rotated-sorted-array/

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.
# You may assume no duplicate exists in the array.
# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1: Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2: Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

def search(nums, target):
    num_len= len(nums)
    if num_len <= 1:
        if nums == []:
            return -1
        elif nums[0] == target:
            return 0
    elif nums[0] == target:
        return 0
    elif nums[0] <= target and nums[1] > nums[0]:
        i = 0
        while i < num_len:
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return - 1
            i += 1
    elif nums[0] > target  and nums[num_len-1] < nums[0]:
        i = num_len -1
        while i >= 0:
            if nums[i] == target:
                return i
            elif nums[i] < target:
                return -1
            i -= 1
    return -1


# Runtime: 48 ms - for test run
# Submission Detail
# 196 / 196 test cases passed.
# Status: Accepted
# Runtime: 36 ms
# Memory Usage: 14.1 MB

# print(search([4,5,6,7,0,1,2],0))
# print(search([4,5,6,7,0,1,2], 3))
print(search([3,2,1], 3))

# better but still O(n)
def search_better(nums, target):
    num_len= len(nums)
    if num_len <= 1:
        if nums == [] or nums[0] != target:
            return -1
        elif nums[0] == target:
            return 0
    elif abs(nums[0]-target) >= abs(nums[1]-target):
        i =1
        while i < num_len:
            if nums[i] == target:
                return i
            i += 1
    elif abs(nums[0]-target) < abs(nums[1]-target):
        i = num_len -1
        while i >= 0:
            if nums[i] == target:
                return i
            i -= 1
    return -1

# Runtime: 28 ms- for test run
# 196 / 196 test cases passed.
# Status: Accepted
# Runtime: 68 ms (very bad end of the not in the distribution - too long)
# Memory Usage: 14.1 MB


# print(search_better([4,5,6,7,0,1,2],0))
# print(search_better([4,5,6,7,0,1,2], 3))

# This is O(n) runtime
def search_on(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

# Rruntime: 32ms - for test run - too long for other results

# print(search_on([4,5,6,7,0,1,2],0))
# print(search_on([4,5,6,7,0,1,2], 3))