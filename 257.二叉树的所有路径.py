#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []
        
        if not root.left and not root.right:
            return [str(root.val)]

        result = []

        child_list = self.binaryTreePaths(root.left) +  self.binaryTreePaths(root.right)
        for content in child_list:
            result.append(str(root.val) + "->"+content)
        
        return result
        
            





# @lc code=end

