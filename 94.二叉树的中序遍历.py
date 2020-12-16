#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.answer = []
        self.dfs(root)
        return self.answer
    
    def update(self,value):
        self.answer.append(value)

    def dfs(self, node):
        if node is None:
            return 
        
        self.dfs(node.left)
        self.update(node.val)
        self.dfs(node.right)
        
# @lc code=end


