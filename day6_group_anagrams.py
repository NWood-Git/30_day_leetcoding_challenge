# Day 6 - Completed 4/6/2020
#  Group Anagrams - 49. Group Anagrams
# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3288/
# https://leetcode.com/problems/group-anagrams/

# Given an array of strings, group anagrams together.

# Example:Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.


def groupAnagrams(strs):
    result = {}
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word not in result.keys():
            result[sorted_word] = [word]
        else:
            result[sorted_word].append(word)
    return result.values()

# Submission Detail
# 101 / 101 test cases passed.
# Status: Accepted
# Runtime: 140 ms / 132 ms
# Memory Usage: 17.1 MB / 16.9 MB
# Your runtime beats 12.53 % of python3 submissions. /
# Your runtime beats 14.42 % of python3 submissions.


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


def groupAnagrams_2(strs):
    result = {}
    for i in strs:
        sorted_letters = "".join(sorted(list(i)))
        if sorted_letters not in result.keys():
            result[sorted_letters] = [i]
        else:
            result[sorted_letters].append(i)
    return list(result.values())

# Submission Detail
# 101 / 101 test cases passed.
# Status: Accepted
# Runtime: 120 ms / 188 ms / 176 ms
# Memory Usage: 16.5 MB / 16.6 MB / 16.3 MB
# Your runtime beats 23.54 % of python3 submissions. /
# Your runtime beats 6.42 % of python3 submissions. /
# Your runtime beats 7.50 % of python3 submissions.

print(groupAnagrams_2(["eat", "tea", "tan", "ate", "nat", "bat"]))