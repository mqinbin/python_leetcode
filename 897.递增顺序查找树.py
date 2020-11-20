#
# @lc app=leetcode.cn id=897 lang=python3
#
# [897] 递增顺序查找树
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
        self.head = None
        self.cur = None

    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.dfs(root)
        return self.head


    def update(self, val):
        node = TreeNode(val)
        if self.head is None:
            self.head = node
            return 
        if self.cur is None:
            self.head.right = node
            self.cur = node
        else:
            self.cur.right = node
            self.cur = node
    def dfs(self, node):
        if node is None:
            return 
        self.dfs(node.left)
        self.update(node.val)
        self.dfs(node.right)


# @lc code=end

