#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode(None)
        leftHead = ListNode(None)
        rightHead = ListNode(None)

        node = head
        left = leftHead
        right = rightHead
        while node:
            if node.val < x:
                left.next = node
                left = left.next
            else:
                right.next = node
                right = right.next
            node = node.next
        left.next = None
        right.next = None
        if leftHead.next:
            dummy.next = leftHead.next
            left.next = rightHead.next
        else:
            dummy.next = rightHead.next
        return dummy.next



# @lc code=end

