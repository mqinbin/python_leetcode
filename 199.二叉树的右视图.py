#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        target = 1
        nones = 0
        stack = [root]
        temp = []
        levels = []
        level_count = 0
        while stack:
            node = stack.pop(0)
            level_count += 1
            temp.append(node.val)
            for child in [node.left,node.right]:
                if child is None:
                    nones += 1
                else:
                    stack.append(child)
                    
            if level_count == target:
                levels.append(temp)
                temp = []
                target = target * 2 - nones
                nones = 0
                level_count = 0
        if temp:
            levels.append(temp)
        print(levels)

        return [t[-1] for t in levels]
# @lc code=end

