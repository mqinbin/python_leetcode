#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        answer = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        answer.left = self.buildTree(preorder[1:mid+1] , inorder[0:mid])
        answer.right = self.buildTree( preorder[mid+1:] ,inorder[mid+1:])


        return answer


# @lc code=end

