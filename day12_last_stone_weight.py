# Day 12 - completed 4/12/2020
# Last Stone Weight - 1046. Last Stone Weight
# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3297/
# https://leetcode.com/problems/last-stone-weight/

# Last Stone Weight
# We have a collection of stones, each stone has a positive integer weight.

# Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

# Example 1: # Input: [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.

# Note:
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000


def lastStoneWeight(stones):
    stones = sorted(stones)
    while len(stones) > 1:
        heaviest_stone = stones.pop(-1)
        next_stone = stones.pop(-1)
        diff = heaviest_stone - next_stone
        stones.append(diff)
        stones = sorted(stones)
    return 0 if stones == [] else stones[0]

# Submission Detail (same 2x)
# 70 / 70 test cases passed.
# Status: Accepted
# Runtime: 24 ms
# Memory Usage: 13.8 MB
# Your runtime beats 93.70 % of python3 submissions.

'''
def lastStoneWeight(stones):
    stones = sorted(stones, reverse=True)
    while len(stones) > 1:
        heaviest_stone = stones.pop(0)
        next_stone = stones.pop(0)
        diff = heaviest_stone - next_stone
        if diff != 0:
            if stones and diff < stones[-1]:
                stones.append(diff)
            else:
                i = 0
                while stones and diff < stones[i] and stones[i] != stones[-1]:
                    i += 1
                stones.insert(i,diff)
    return 0 if stones == [] else stones[0]
'''
# Submission Detail
# 70 / 70 test cases passed.
# Status: Accepted
# Runtime: 20 ms / 24 ms (2x) / 28ms (2x)
# Memory Usage: 14 MB / 13.9 MB / 13.7 / 13.8 (2x) 
# Your runtime beats 98.60 % of python3 submissions.
# Your runtime beats 93.70 % of python3 submissions (2x).
# Your runtime beats 75.18 % of python3 submissions(2x).


print(lastStoneWeight([2,7,4,1,8,1])) # 1
print(lastStoneWeight([2,7,4,1,8,1,1])) # 0
print(lastStoneWeight([3,7,8])) # 2
print(lastStoneWeight([6,2,2,7])) #1