#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:
            return None

        fast = head
        slow = head
        tail = None

        while fast and fast.next:
            tail = slow
            slow = slow.next
            fast = fast.next.next

        node = TreeNode(slow.val)
        if tail:
            tail.next = None
            node.left = self.sortedListToBST(head)
            node.right = self.sortedListToBST(slow.next)

        return node
        
# @lc code=end

