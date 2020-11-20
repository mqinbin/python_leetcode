#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树节点最小距离
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
        self.answer = 2 ** 31
        self.last_val = -2 ** 31     

    def minDiffInBST(self, root: TreeNode) -> int:
        self.midTravel(root)
        return self.answer

    def update(self, val):
        self.answer = min(self.answer ,  val - self.last_val  )
        self.last_val = val


    def midTravel(self, node):
        if node is None:
            return 

        self.midTravel(node.left)
        self.update(node.val)
        self.midTravel(node.right)
# @lc code=end

