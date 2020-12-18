#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if root is None:
            return None
        
        if root.left is None  and root.right is None:
            return root

        leftPart = self.flatten(root.left)
        rightPart = self.flatten(root.right)
        if leftPart:
            root.left = None
            root.right = leftPart
            if rightPart:
                while leftPart.right:
                    leftPart = leftPart.right
                leftPart.right = rightPart

        return root


# @lc code=end

