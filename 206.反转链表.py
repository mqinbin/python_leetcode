#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        pre = None
        cur = head
        next = cur.next
        while next:
            cur.next= pre
            pre = cur
            cur = next
            next = next.next
        cur.next = pre
        return cur

# @lc code=end

