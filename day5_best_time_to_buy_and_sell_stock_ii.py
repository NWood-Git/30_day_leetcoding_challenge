# Day 5 - Completed 4/5/2020
# Best Time to Buy and Sell Stock II - 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3287/
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (i.e., buy one and sell one share of the stock multiple times).

# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

# Example 1:Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

# Example 2:Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
# engaging multiple transactions at the same time. You must sell before buying again.

# Example 3:Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
def maxProfit(prices):
    if len(prices) < 2: return 0
    profits = []
    for i in range(1,len(prices)):
        if prices[i] > prices[i-1]:
            profits.append(prices[i] - prices[i-1])
    return sum(profits)

# Submission Detail
# 201 / 201 test cases passed.
# Status: Accepted
# Runtime: 56 ms
# Memory Usage: 14.9 MB
# Your runtime beats 92.70 % of python3 submissions.

print(maxProfit([7,1,5,3,6,4])) # 7
print(maxProfit([1,2,3,4,5])) # 4
print(maxProfit([7,6,4,3,1])) # 0

def maxProfit_med(prices):
    px_len = len(prices)
    if px_len < 0:
        return 0
    else:
        profits = []
        for i in range(0,px_len-1):
            px = prices[i]
            next_px = prices[i+1]
            if px < next_px:
                profits.append(next_px-px)
    return sum(profits)

# Submission Detail
# 201 / 201 test cases passed.
# Status: Accepted
# Runtime: 64 ms
# Memory Usage: 15.3 MB
# Your runtime beats 47.12 % of python3 submissions.    

# print(maxProfit_med([7,1,5,3,6,4])) # 7
# print(maxProfit_med([1,2,3,4,5])) # 4
# print(maxProfit_med([7,6,4,3,1])) # 0


def maxProfit_slow(prices):
    px_len = len(prices)
    if px_len <= 1:
        return 0
    else:
        low = prices[0]
        profit = 0
        for i in range(1,px_len):
            next_px = prices[i]
            if low < next_px:
                profit += (next_px-low)
            low = next_px
    return profit

# Success Detail
# 201 / 201 test cases passed.
# Status: Accepted
# Runtime: 100 ms
# Memory Usage: 15.1 MB
# Really bad runtime - doesn't beat any results

# print(maxProfit_slow([7,1,5,3,6,4])) # 7
# print(maxProfit_slow([1,2,3,4,5])) # 4
# print(maxProfit_slow([7,6,4,3,1])) # 0
