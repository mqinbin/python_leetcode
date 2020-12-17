#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        stack = []
        dummy = ListNode(None)
        dummy.next = head
        cur = dummy
        passed = 0
        part_one_last = None
        part_three_first = None
        while cur:
            passed += 1
            if passed == m:
                part_one_last = cur
            cur = cur.next
            if passed >= m:
                stack.append(cur)
            if passed == n:
                part_three_first = cur.next
                break
        # print(part_one_last.val , part_three_first.val)
        # print(*map(lambda n: n.val , stack ))
        while stack:
            node =stack.pop()
            part_one_last.next = node
            part_one_last = node
        
        part_one_last.next = part_three_first

        return dummy.next


# @lc code=end

