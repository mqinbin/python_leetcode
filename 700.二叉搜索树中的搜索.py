#
# @lc app=leetcode.cn id=700 lang=python3
#
# [700] 二叉搜索树中的搜索
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root.val == val:
            return root

        if root.val > val:
            if root.left:
                return self.searchBST(root.left,val)
            else:
                return None
        if root.val < val:
            if root.right:
                return self.searchBST(root.right,val)
            else:
                return None
        
# @lc code=end

