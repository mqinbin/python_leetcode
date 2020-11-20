#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        result = 0 
        if root:
            if root.left :
                if self.is_leaf(root.left):
                    result += root.left.val
                else:
                    result += self.sumOfLeftLeaves(root.left)
            if root.right:
                result += self.sumOfLeftLeaves(root.right)
        
        return result
    
    def is_leaf(self, root):
        return  root  and root.left is None and root.right is None
# @lc code=end

