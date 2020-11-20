#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.height(root) != -1

    def height(self, node: TreeNode) -> int:
        if not node:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        if left_height == -1 or right_height == -1 or abs(left_height - right_height ) > 1:
            return -1
        return max(left_height,right_height) + 1
# @lc code=end

