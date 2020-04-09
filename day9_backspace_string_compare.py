# Day 8 - Completed 4/9/2020
# Backspace String Compare - 844. Backspace String Compare
# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3291/
# https://leetcode.com/problems/backspace-string-compare/

# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

# Example 1: Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".

# Example 2: Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".

# Example 3: Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".

# Example 4: Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".

# Note:
# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.

# Follow up: Can you solve it in O(N) time and O(1) space?

def backspaceCompare(S, T):
    def new_str(strng):
        result = []
        for i in strng:
            if i != '#':
                result.append(i)
            elif result:
                result.pop()
        return result
    return new_str(S) == new_str(T)

# Submission Detail
# 104 / 104 test cases passed.
# Status: Accepted
# Runtime: 28 ms / 28 ms
# Memory Usage: 14 MB / 13.7 MB
# Your runtime beats 70.73 % of python3 submissions.
# Your runtime beats 70.73 % of python3 submissions.

'''
def backspaceCompare(S, T):
    new_s = []
    new_t = []
    for i in S:
        if i != '#':
            new_s.append(i)
        else:
            new_s = new_s[:-1]
    for i in T:
        if i != '#':
            new_t.append(i)
        else:
            new_t = new_t[:-1]
    return new_s == new_t
'''
# Submission Detail
# 104 / 104 test cases passed.
# Status: Accepted
# Runtime: 24 ms / 32ms
# Memory Usage: 13.8 MB / 13.8MB
# Your runtime beats 90.48 % of python3 submissions.
# Your runtime beats 35.38 % of python3 submissions.

'''
def backspaceCompare(S, T):
    new_s = []
    new_t = []
    for i in S:
        if i != '#':
            new_s.append(i)
        else:
            new_s = new_s[:-1]
    for i in T:
        if i != '#':
            new_t.append(i)
        else:
            new_t = new_t[:-1]
    return "".join(new_s) == "".join(new_t)
'''    

# Submission Detail
# 104 / 104 test cases passed.
# Status: Accepted
# Runtime: 28 ms
# Memory Usage: 13.6 MB
# Your runtime beats 70.73 % of python3 submissions.


print(backspaceCompare("ab#c", "ad#c"))
print(backspaceCompare("ab##", "c#d#"))
print(backspaceCompare("a##c", "#a#c"))
print(backspaceCompare("a#c", "b"))