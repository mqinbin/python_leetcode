#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.init = float('-inf')

        try:
            self.dfs(root)
        except:
            return False
        return True


    def update(self,value):
        if value > self.init:
            self.init = value
        else:
            raise Exception
    
    def dfs(self, node):
        if node is None:
            return 
        
        self.dfs(node.left)
        self.update(node.val)
        self.dfs(node.right)

# @lc code=end

