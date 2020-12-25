#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根到叶子节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.total = 0
        self.dfs(root, 0)
        return self.total


    def update(self,value):
        self.total  += value

    def dfs(self,node, parentsValue):
        if node is None:
            return 
        value = node.val + parentsValue * 10
        if node.left is None and node.right is None:
            self.update(value)
        
        self.dfs(node.left , value)
        self.dfs(node.right , value)


# @lc code=end

