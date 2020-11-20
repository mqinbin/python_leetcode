#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
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
    def preorder(self, root: 'Node') -> List[int]:
        
        self.dfs(root)


        return self.result

    def __init__(self):
        self.result = []

    def update(self, val):
        self.result.append(val)

    def dfs(self, node):
        if node is None:
            return
        self.update(node.val)
        for child in node.children:
            self.dfs(child)
        
# @lc code=end

