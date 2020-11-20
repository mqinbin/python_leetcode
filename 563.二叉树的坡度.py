#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = 0
    def findTilt(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.result

    def update(self, val):
        self.result +=val

    def dfs(self, node):
        if node is None:
            return 0

        left_sum = self.dfs(node.left)
        right_sum = self.dfs(node.right)
        
        self.update(abs(left_sum - right_sum))
        return node.val + left_sum + right_sum
    
        
        

# @lc code=end

