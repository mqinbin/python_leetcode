#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.answer =[]

        self.dfs(root,sum,[])

        return self.answer

    def update(self, path):
        self.answer.append(path)

    def dfs(self, node, target, path):
        if not node:
            return

        if not node.left and not node.right:
            if node.val == target:
                self.update(path+[node.val])
            return 
        self.dfs(node.left , target-node.val , path+[node.val]) 
        self.dfs(node.right , target-node.val , path+[node.val]) 
# @lc code=end
