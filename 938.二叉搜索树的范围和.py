#
# @lc app=leetcode.cn id=938 lang=python3
#
# [938] 二叉搜索树的范围和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.answer = 0
        self.dfs(root , low, high)
        return self.answer
    
    def dfs(self, node, low,high):
        if node is None:
            return 
        
        if low <= node.val <= high:
            self.answer += node.val

        if node.val <= low:
            self.dfs(node.right , low, high)
        elif node.val >= high:
            self.dfs(node.left  , low, high)
        else:
            self.dfs(node.right , low, high)
            self.dfs(node.left  , low, high)





# @lc code=end

