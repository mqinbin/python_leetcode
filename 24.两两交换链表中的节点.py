#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None  or head.next is None:
            return head
            
        next = head.next
        head.next  = self.swapPairs(next.next)
        next.next = head
        return next


        





        
# @lc code=end

