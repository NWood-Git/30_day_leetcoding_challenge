# Day 16 - Completed 4/17/2020 - Early AM
# Difficulty - Medium
# Valid Parenthesis String - 678. Valid Parenthesis String
# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3301/
# https://leetcode.com/problems/valid-parenthesis-string/

# Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# An empty string is also valid.

# Example 1: Input: "()"
# Output: True
# Example 2: Input: "(*)"
# Output: True
# Example 3: Input: "(*))"
# Output: True
# Note: The string size will be in the range [1, 100].

def checkValidString(s):
    if len(s) == 0 or s == '*':
        return True
    if len(s) ==1:
        return False
    
    left_bal = 0
    for i in s:
        if i == ')':
            left_bal -= 1
        else:
            left_bal += 1
        
        if left_bal < 0:
            return False
        
    if left_bal == 0:
        return True

    right_bal = 0
    for i in reversed(s):
        if i == '(':
            right_bal -= 1
        else:
            right_bal += 1
        if right_bal < 0:
            return False

    return True

# Submission Detail
# 58 / 58 test cases passed.
# Status: Accepted
# Runtime: 24 ms
# Memory Usage: 13.8 MB
# Your runtime beats 90.64 % of python3 submissions.


print(checkValidString("()"))
print(checkValidString("(*)"))
print(checkValidString("(*))"))

# Good Explanation: https://www.youtube.com/watch?v=S2LX5E8uxSw















# def checkValidString(s):
#     left = 0
#     l_temp
#     right = 0
#     r_temp =0
#     star = 0
#     for i in s:
#         if i == '(':
#             if right > 0:
#                 right -= 1
#             else:
#                 left += 1
#         elif i == ')':
#             if left > 0:
#                 left -= 1
#             else:
#                 right += 1
#         elif i == '*':
#             if left > 0 and right == 0:
#                 left -= 1
#             elif right > 0 and left == 0:
#                 right -= 1
#             elif left == 0 and right == 0:
#                 pass #* is empty string
#             else:
#                 star += 1
#                 r_temp = right
#                 l_temp = left
#     if star > 0:
#         if right > star > 0  and r_temp > 0 :

        
