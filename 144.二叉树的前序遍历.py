#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.answer = []

        self.dfs(root)
        return self.answer
        
    def update(self, value):
        self.answer.append(value)

    def dfs(self,node):
        if node is None:
            return 
        
        self.update(node.val)
        self.dfs(node.left)
        self.dfs(node.right)
# @lc code=end

