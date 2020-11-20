#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
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
        self.acc= 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        self.dfs(root)
        return root


    def update(self, node):
        val = node.val
        node.val +=self.acc
        self.acc +=val


    def dfs (self, node):
        if node is None:
            return 
        self.dfs(node.right)
        self.update(node)
        self.dfs(node.left)

# @lc code=end

