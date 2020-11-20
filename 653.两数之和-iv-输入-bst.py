#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if root is None:
            return False

        return self._findTarget(root, set() , k)
            

    def _findTarget(self, node: TreeNode, node_values:set,k: int) -> bool:
        if node is None:
                return False
        other_val = k - node.val
        if other_val in node_values:
            return True
        node_values.add(node.val)
        return self._findTarget(node.left, node_values ,k) or self._findTarget(node.right, node_values ,k) 
# @lc code=end

