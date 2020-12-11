#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        n = 1
        tail = head
        while tail.next:
            n += 1
            tail = tail.next
        tail.next = head        
        k= k % n
        temp = head
        for _ in range(n - k - 1):
            temp =temp.next
        
        answer = temp.next
        temp.next= None
        return answer


# @lc code=end

