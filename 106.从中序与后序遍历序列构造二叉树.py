#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        if len(postorder) == 0:
            return None
        if len(postorder) == 1:
            return TreeNode(postorder[0])

        node = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])
        node.left = self.buildTree(inorder[:mid] , postorder[:mid])
        node.right = self.buildTree(inorder[mid+1:] , postorder[mid:-1])

        return node



# @lc code=end

