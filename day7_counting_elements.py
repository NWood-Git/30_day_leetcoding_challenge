# Day 7 - Completed 4/7/2020
# Counting Elements
# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3289/

# Given an integer array arr, count element x such that x + 1 is also in arr.

# If there're duplicates in arr, count them seperately.

# Example 1:Input: arr = [1,2,3]
# Output: 2
# Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

# Example 2:Input: arr = [1,1,3,3,5,5,7,7]
# Output: 0
# Explanation: No numbers are counted, cause there's no 2, 4, 6, or 8 in arr.

# Example 3: Input: arr = [1,3,2,3,5,0]
# Output: 3
# Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.

# Example 4: Input: arr = [1,1,2,2]
# Output: 2
# Explanation: Two 1s are counted cause 2 is in arr.

# Constraints:
# 1 <= arr.length <= 1000
# 0 <= arr[i] <= 1000

def countElements(arr):
    result = 0
    arr_len_minus_1 = len(arr) - 1
    arr = sorted(arr)
    for i in range(arr_len_minus_1):
        num = arr[i]
        next_idx = i+1
        while  next_idx < arr_len_minus_1  and arr[next_idx] == num:
            next_idx += 1
        if arr[next_idx] == num + 1:
            result += 1
    return result

# Submission Detail
# 35 / 35 test cases passed.
# Status: Accepted
# Runtime: 28 ms / 24 ms
# Memory Usage: 13.9 MB / 13.8 MB
# Sorry. We do not have enough accepted submissions to show distribution chart.

'''
def countElements(arr):
    result = 0
    for i in arr:
        if i+1 in arr:
            result +=1
    return result
'''
# Submission Detail
# 35 / 35 test cases passed.
# Status: Accepted
# Runtime: 60 ms
# Memory Usage: 14.1 MB
# Sorry. We do not have enough accepted submissions to show distribution chart.

'''
def countElements(arr):
    result = []
    for i in arr:
        if i+1 in result or i+1 in arr:
            result.append(i)
    return len(result)
'''

# Submission Detail
# 35 / 35 test cases passed.
# Status: Accepted
# Runtime: 60 ms
# Memory Usage: 13.8 MB
# Sorry. We do not have enough accepted submissions to show distribution chart.


print(countElements([1,2,3])) # 2
print(countElements([1,1,3,3,5,5,7,7])) # 0
print(countElements([1,3,2,3,5,0])) # 3
print(countElements([1,1,2,2])) # 2