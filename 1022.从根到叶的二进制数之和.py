#
# @lc app=leetcode.cn id=1022 lang=python3
#
# [1022] 从根到叶的二进制数之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.answer = 0
        self.dfs(root, 0)
        return self.answer %  (10**9 + 7)
    
    def update(self, val):
        print(val)
        self.answer += val

    def dfs(self, node, cur):
        if node is None:
            return 
        
        if node.left is None and node.right is None:
            self.update(cur * 2 + node.val)
            return 

        self.dfs(node.left, cur * 2 + node.val)
        self.dfs(node.right, cur * 2 + node.val)


# @lc code=end

