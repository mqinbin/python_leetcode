#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        
        if root.left:
            if root.right:
                root.left.next = root.right 
            if root.left.left or root.left.right:
                pre = root.left.right or root.left.left
                if root.right:
                    n =  root.right.left or root.right.right
                    pre.next = n
            self.connect(root.left)
        self.connect(root.right)
        return root


        
# @lc code=end

