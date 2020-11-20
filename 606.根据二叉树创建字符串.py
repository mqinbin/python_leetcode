#
# @lc app=leetcode.cn id=606 lang=python3
#
# [606] 根据二叉树创建字符串
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        self.dfs(t)
        return self.result
    def __init__(self):
        self.result = ""

    def update(self, val):
        self.result +=val
        
    def dfs(self, node:TreeNode):
        if node is None:
            return

        self.update(str(node.val))
        if node.left:
            self.update("(")
            self.dfs(node.left)
            self.update(")")
        elif node.right:
            self.update("()")

        if node.right:
            self.update("(")
            self.dfs(node.right)
            self.update(")")



# @lc code=end

