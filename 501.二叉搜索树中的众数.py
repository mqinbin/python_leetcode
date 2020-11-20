#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
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
        self.result = []
        self.pre = None
        self.max_count = 0
        self.count = 0

    def findMode(self, root: TreeNode) -> List[int]:
        self.dfs(root)
        return self.result

    def update(self, val):
        if val == self.pre:
            self.count += 1
        else:
            self.count = 1
            self.pre = val

        if self.count > self.max_count:
            self.result.clear()
            self.result.append(val)
            self.max_count = self.count
        elif self.count == self.max_count:
            self.result.append(val)

    def dfs(self, node):
        if node is None:
            return
        self.dfs(node.left)
        self.update(node.val)
        self.dfs(node.right)


# @lc code=end

