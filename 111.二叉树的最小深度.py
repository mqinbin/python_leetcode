#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if None in [root.left,root.right]:
            return max(self.minDepth(root.left),self.minDepth(root.right)) + 1
        else:
            return min(self.minDepth(root.left),self.minDepth(root.right)) + 1
# @lc code=end

