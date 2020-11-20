#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N叉树的最大深度
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        return self.depth(root)

    def depth(self,node):
        if node is None:
            return 0
        if not node.children:
            return 1
        return max(map(self.depth , node.children)) + 1
# @lc code=end

