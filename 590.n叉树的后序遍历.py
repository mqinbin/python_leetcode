#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N叉树的后序遍历
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
    def postorder(self, root: 'Node') -> List[int]:
        self.dfs(root)
        return self.result
    
    def __init__(self):
        self.result = []

    def update(self, val):
        self.result.append(val)

    def dfs(self, node):
        if node is None:
            return
        # for child in reversed(node.children):
        for child in node.children:
            self.dfs(child)
        self.update(node.val)
# @lc code=end

