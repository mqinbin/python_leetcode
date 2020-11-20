#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        
        if not fast:
            return slow.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        

        slow.next = slow.next.next
        return head



# @lc code=end

