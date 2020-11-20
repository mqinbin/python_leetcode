#
# @lc app=leetcode.cn id=671 lang=python3
#
# [671] 二叉树中第二小的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:

        q = [root]
        vals = [root.val]
        while q:
            cur = q.pop(0)
            if cur.val >vals[0]:
                vals.append(cur.val)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        if len(vals) == 1:
            return -1
        
        return sorted(vals)[1]

# @lc code=end

