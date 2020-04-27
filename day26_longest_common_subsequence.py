# Day 26 - Completed 4/_/2020
# Difficulty - Medium
# Longest Common Subsequence - 1143. Longest Common Subsequence
# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/531/week-4/3311/
# https://leetcode.com/problems/longest-common-subsequence/

# Given two strings text1 and text2, return the length of their longest common subsequence.

# A subsequence of a string is a new string generated from the original string with
# some characters(can be none) deleted without changing the relative order of the 
# remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not).
# A common subsequence of two strings is a subsequence that is common to both strings.

# If there is no common subsequence, return 0.

# Example 1: Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.

# Example 2: Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.

# Example 3: Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.

# Constraints:
# 1 <= text1.length <= 1000
# 1 <= text2.length <= 1000
# The input strings consist of lowercase English characters only.

def longestCommonSubsequence(text1, text2):
    n,m = len(text1), len(text2)
    dp = [[0] * (m+1) for z in range(n+1)]
    for i in range(n):
        for j in range(m):
            if text1[i] == text2[j]:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[-1][-1]


# 37 / 37 test cases passed.
# Status: Accepted
# Runtime: 404 ms
# Memory Usage: 21.3 MB
# Your runtime beats 89.57 % of python3 submissions

print(longestCommonSubsequence("abcde", "ace"))
print(longestCommonSubsequence("abc", "abc"))
print(longestCommonSubsequence("abc", "def"))


# Refrence:
# https://www.youtube.com/watch?v=FWyANT-7iq8