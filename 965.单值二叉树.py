#
# @lc app=leetcode.cn id=965 lang=python3
#
# [965] 单值二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        answer = True
        if root.left:
            answer &= root.val == root.left.val  and self.isUnivalTree(root.left)
        if root.right:
            answer &= root.val == root.right.val  and self.isUnivalTree(root.right)
        return answer
# @lc code=end

