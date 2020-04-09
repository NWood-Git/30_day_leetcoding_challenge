# Day 8 - Completed 4/8/2020
# Middle of the Linked List - 876. Middle of the Linked List
# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3290/
# https://leetcode.com/problems/middle-of-the-linked-list/

# Given a non-empty, singly linked list with head node head, return a middle node of linked list.

# If there are two middle nodes, return the second middle node.

# Example 1: Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

# Example 2: Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second one.

# Note: The number of nodes in the given list will be between 1 and 100.

def middleNode(head):
    fast = slow = head
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next
    return slow

# Submission Detail
# 15 / 15 test cases passed.
# Status: Accepted
# Runtime: 32 ms
# Memory Usage: 13.7 MB
# Your runtime beats 18.70 % of python3 submissions.

#TODO: Build Linked List to test this solution in this file

# print(middleNode([1,2,3,4,5]))


# Solution Video - Youtube
# https://www.youtube.com/watch?v=BafeN6aLTOY

# Solution Article: Leetcode
# https://leetcode.com/articles/middle-of-the-linked-list/