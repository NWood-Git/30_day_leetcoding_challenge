# Day 4 - Completed 4/5/2020 (early AM)
# Moves Zeroes - 283. Move Zeroes
# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3286/
# https://leetcode.com/problems/move-zeroes/

# Given an array nums, write a function to move all 0's to the end of it 
# while maintaining the relative order of the non-zero elements.

# Example: Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Note: You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

def moveZeroes(nums):
    idx = 0
    num_len = len(nums)
    if num_len <= 1:
        return nums
    else:
        for i in range(len(nums)):
            if nums[idx] == 0:
                del nums[idx]
                nums.append(0)
            else:
                idx += 1
    return nums

# Submission Detail
# 21 / 21 test cases passed.
# Status: Accepted
# Runtime: 44 ms / 36 ms
# Memory Usage: 15 MB / 15.1 MB
# Your runtime beats 90.64 % of python3 submissions. / Your runtime beats 99.52 % of python3 submissions.

print(moveZeroes([0,1,0,3,12]))
print(moveZeroes([0,0,1]))



def moveZeroes(nums):
    idx = 0
    for i in range(len(nums)):
        if nums[idx] == 0:
            del nums[idx]
            nums.append(0)
        else:
            idx += 1

# Submission Detail
# 21 / 21 test cases passed.
# Status: Accepted
# Runtime: 48 ms
# Memory Usage: 15.1 MB
# Your runtime beats 73.09 % of python3 submissions.

nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)

nums = [0,0,1]
moveZeroes(nums)
print(nums)

def moveZeroes_count(nums):
    idx=0
    num_zeroes = 0
    for i in range(len(nums)):
        if nums[idx] == 0:
            del nums[idx]
            num_zeroes += 1
        else:
            idx += 1
    for i in range(num_zeroes):
        nums.append(0)

# Submission Detail
# 21 / 21 test cases passed.
# Status: Accepted
# Runtime: 52 ms
# Memory Usage: 15.1 MB
# Your runtime beats 44.16 % of python3 submissions.

# nums = [0,1,0,3,12]
# moveZeroes_count(nums)
# print(nums)

# nums = [0,0,1]
# moveZeroes_count(nums)
# print(nums)


def moveZeroes_rm(nums):
    for num in nums:
        if num == 0:
            nums.remove(0)
            nums.append(0)

# Submission Detail
# 21 / 21 test cases passed.
# Status: Accepted
# Runtime: 232 ms
# Memory Usage: 15.1 MB
# Your runtime beats 11.53 % of python3 submissions.

# nums = [0,1,0,3,12]
# moveZeroes_rm(nums)
# print(nums)
