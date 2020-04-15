# Day 14 - Completed 4/14/2020
# Difficulty Medium
# Perform String Shifts - 796. Rotate String
# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3299/
# https://leetcode.com/problems/rotate-string/

# Perform String Shifts
# You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

# direction can be 0 (for left shift) or 1 (for right shift). 
# amount is the amount by which string s is to be shifted.
# A left shift by 1 means remove the first character of s and append it to the end.
# Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
# Return the final string after all operations.

# Example 1: Input: s = "abc", shift = [[0,1],[1,2]]
# Output: "cab"
# Explanation: 
# [0,1] means shift to left by 1. "abc" -> "bca"
# [1,2] means shift to right by 2. "bca" -> "cab"

# Example 2: Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
# Output: "efgabcd"
# Explanation:  
# [1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
# [1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
# [0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
# [1,3] means shift to right by 3. "abcdefg" -> "efgabcd"

# Constraints:
# 1 <= s.length <= 100
# s only contains lower case English letters.
# 1 <= shift.length <= 100
# shift[i].length == 2
# 0 <= shift[i][0] <= 1
# 0 <= shift[i][1] <= 100

def stringShift(s, shift):
    move_left = 0
    length_of_string = len(s)
    for direction, amount in shift:
        if direction == 0:
            move_left = move_left + amount
        else:
            move_left -= amount
    move_left = move_left % length_of_string
    return s[move_left:] + s[:move_left]

# 31 / 31 test cases passed.
# Status: Accepted
# Runtime: 24 ms
# Memory Usage: 13.9 MB
    
print(stringShift("abcdefg", [[1,1],[1,1],[0,2],[1,3]])) # "efgabcd"
print(stringShift("abc", [[0,1],[1,2]])) # "cab


def stringShift(s, shift):
    for item in shift:
        if item[0] == 0: # left
            shifted = s[:item[1]]
            static = s[item[1]:]
            s = static + shifted
        elif item[0] == 1:
            shifted = s[-item[1]:]
            static = s[:-item[1]]
            s = shifted + static
    return s

# Submission Detail
# 31 / 31 test cases passed.
# Status: Accepted
# Runtime: 28 ms /  36 ms
# Memory Usage: 14.1 MB / 13.8 MB

# print(stringShift("abcdefg", [[1,1],[1,1],[0,2],[1,3]])) # "efgabcd"
# print(stringShift("abc", [[0,1],[1,2]])) # "cab"



# better solution from https://www.youtube.com/watch?v=Ck4enzniqQo