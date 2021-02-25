#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(float('-inf'))
        dummy.next = head

        pre = dummy.next
        while pre:
            cur = pre.next
            if cur and cur.val < pre.val:
                start = dummy
                while start.next.val < cur.val:
                    start = start.next
                else:
                    pre.next = cur.next
                    cur.next = start.next
                    start.next = cur
            else:
                pre = pre.next


        return dummy.next




# @lc code=end

