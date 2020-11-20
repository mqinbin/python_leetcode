#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
            
        return self._isSymmetric(root.left, root.right)

    def _isSymmetric(self, p: TreeNode,q: TreeNode) -> bool:
        if p is None  and q is None:
            return True
        if p is None and q is not None:
            return False
        if p is not None and q is None:
            return False
        return p.val== q.val and self._isSymmetric(p.left,q.right) and self._isSymmetric(p.right,q.left)
# @lc code=end

