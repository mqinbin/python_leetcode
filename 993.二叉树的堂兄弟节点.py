#
# @lc app=leetcode.cn id=993 lang=python3
#
# [993] 二叉树的堂兄弟节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        xp = []
        self.dfs(root,x,xp)
        yp = []
        self.dfs(root,y,yp)


        if len(xp) != len(yp):
            return False
        if len(xp) < 3 or len(yp)<3:
            return False

        return  xp[-2] != yp[-2]

    
    def dfs(self, node,value, parents):
        if not node:
            return False
        
        if node.val != value and not node.left and not node.right:
            return False
        
        if node.val == value:
            parents.append(node)
            return True

        parents.append(node)
        if self.dfs(node.left,value,parents):
            return True
        
        while parents:
            if parents.pop() ==node:
                break
        
        parents.append(node)
        if self.dfs(node.right,value,parents):
            return True 
        
        while parents:
            if parents.pop() ==node:
                break
        return False
        
# @lc code=end

