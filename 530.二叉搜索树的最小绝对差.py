#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.pre = None
        self.min_diff = 2 ** 31

    def getMinimumDifference(self, root: TreeNode) -> int:

        self.dfs(root)

        return self.min_diff

    def dfs(self, node):

        if node is None:
            return 
        
        self.dfs(node.left)
        self.update(node.val)
        self.dfs(node.right)

    def update(self, val):
        if self.pre is None:
            self.pre = val
            return 
        
        self.min_diff = min(self.min_diff, abs(self.pre -  val))
        self.pre =  val

# @lc code=end

