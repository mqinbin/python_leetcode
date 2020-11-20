#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        lh = self.height(root.left)
        rh =  self.height(root.right)
        print(lh,rh)
        return  lh + rh +  bool(lh) + bool(rh )
    
    def height(self, node):
        if node is None:
            return 0
        if not node.left and not node.right:
            return 0
        return max(self.height(node.left),self.height(node.right) ) + 1

        
# @lc code=end

