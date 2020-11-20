#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一个树的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        stack = []
        stack.append(s)
        while stack:
            cur = stack.pop()
            if self.isSameTree(cur,t):
                return True
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        
        return False



    def isSameTree(self, first,second):
        if first is None and second is None:
            return True
        
        if first is None or second is None:
            return False

        return first.val == second.val \
            and self.isSameTree(first.left,second.left) \
            and   self.isSameTree(first.right,second.right) 
        
# @lc code=end

