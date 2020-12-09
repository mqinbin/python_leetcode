#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        def getNodeValue(node):
            if node is None:
                return 0
            else:
                return node.val
        
        result = ListNode()
        cur1 = l1
        cur2 = l2
        curResult = result
        carry = 0
        while True:
            carry,thisDig = divmod(getNodeValue(cur1) + getNodeValue(cur2) + carry ,10)
            curResult.val = thisDig

            cur1 = None if cur1 is None else cur1.next
            cur2 = None if cur2 is None else cur2.next
            if not carry and cur1 is None and cur2 is None:
                break
            else:
                curResult.next = ListNode()
                curResult = curResult.next
        return result


    # def addTwoNumbers(self, l1, l2):
    #     """
    #     :type l1: ListNode
    #     :type l2: ListNode
    #     :rtype: ListNode
    #     """
    #     cur = result = None

    #     while l1 or l2:
    #         e = (l1.val if l1 else 0) + (l2.val if l2 else 0)
    #         if cur is None:
    #             cur = result =  ListNode(e)
    #         else :
    #             cur.next = ListNode(e)
    #             cur = cur.next
            
    #         l1 = l1.next if l1 else None
    #         l2 = l2.next if l2 else None

    #     cur = result
    #     while cur:
    #         if cur.val >= 10:
    #             if cur.next:
    #                 cur.next.val += 1
    #             else:
    #                 cur.next = ListNode(1)
    #             cur.val = cur.val - 10
    #         cur = cur.next

    #     return result




# @lc code=end
