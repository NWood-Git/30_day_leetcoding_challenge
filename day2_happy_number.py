# Day 2 - Completed 4/2/2020
# Happy Number
# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3284/

# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, 
# replace the number by the sum of the squares of its digits, and repeat the process 
# until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
# Those numbers for which this process ends in 1 are happy numbers.

# Example: Input: 19
# Output: true
# Explanation: 
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

# Note the count of 6 is take from the notes below

def isHappy_wl(n):
    count = 0
    while n != 1:
        count += 1 
        if count == 7:
            return False
        else:
            n_lst = [int(i) for i in str(n)]
            n = 0
            for i in n_lst:
                n += i**2
    return True

# Submission Detail
# 401 / 401 test cases passed.
# Status: Accepted
# Runtime: 20 ms
# Memory Usage: 14 MB
# Your runtime beats 99.38 % of python3 submissions.

print(isHappy_wl(19)) # True
print(isHappy_wl(22)) # False
print(isHappy_wl(23)) # True


def isHappy_rc(n, count=0):
    n = [int(i) for i in str(n)]
    new_n = 0
    for i in n:
        new_n += i**2
    if new_n == 1:
        return True
    elif count == 6:
        return False
    else:
        count += 1
        return isHappy_rc(new_n, count) # for leetcode - self.isHappy(new_n, count)

# Submission Detail
# 401 / 401 test cases passed.
# Status: Accepted
# Runtime: 32 ms
# Memory Usage: 13.7 MB
# Your runtime beats 66.89 % of python3 submissions.


# print(isHappy_rc(19)) # True
# print(isHappy_rc(22)) # False
# print(isHappy_rc(23)) # True


# Using recursion with try / except - on Leetcode - Status - Time Limit Exceeded

def isHappy_rte(n, count=0):
    n = [int(i) for i in str(n)]
    new_n = 0
    for i in n:
        new_n += i**2
    if new_n == 1:
        return True
    elif count == 6:
        return False
    else:
        count += 1
        try:
            return isHappy_rte(new_n) # for leetcode - self.isHappy(new_n)
        except RecursionError:
            return False

# print(isHappy_rte(19)) # True
# print(isHappy_rte(22)) # False
# print(isHappy_rte(23)) # True


# Used info from: https://mathworld.wolfram.com/HappyNumber.html

# Let the sum of the squares of the digits of a positive integer s_0 be represented by s_1. 
# In a similar way, let the sum of the squares of the digits of s_1 be represented by s_2, and so on.
# Iterating this sum-of-squared-digits map always 
# eventually reaches one of the 10 numbers 0, 1, 4, 16, 20, 37, 42, 58, 89, or 145 (OEIS A039943; Porges 1945).
# If s_i=1 for some i>=1, then the original integer s_0 is said to be happy. 
# For example, starting with 7 gives the sequence 7, 49, 97, 130, 10, 1, so 7 is a happy number.
# The first few happy numbers are 1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 
# 79, 82, 86, 91, 94, 97, 100, ... (OEIS A007770). 
# These are also the numbers whose 2-recurring digital invariant sequences have period 1. 
# The numbers of iterations required for these to reach 1 are 0, 5, 1, 2, 4, 3, 3, 2, 3, 4, 4, 2, 5, ... (OEIS A090425).