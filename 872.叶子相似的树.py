#
# @lc app=leetcode.cn id=872 lang=python3
#
# [872] 叶子相似的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leafs1 = []
        self.dfs(root1,leafs1)

        leafs2 = []
        self.dfs(root2,leafs2)

        # print(leafs1)
        # print(leafs2)
        return leafs1 == leafs2


    def dfs(self, node, leafs):
        if node is None:
            return 
        if node.left is None and node.right is None:
            leafs.append(node.val)
            return 
        
        self.dfs(node.left,leafs)
        self.dfs(node.right,leafs)
# @lc code=end

