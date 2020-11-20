#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        stack = [(root,0)]
        
        cur_level = -1
        level_sum = 0
        level_count = 0
        result = []
        while stack:
            node, lv = stack.pop()
            
            if node.left:
                stack.append((node.left, lv+1))
            if node.right:
                stack.append((node.right, lv+1))

            if lv == cur_level:
                level_sum += node.val
                level_count += 1
            else:
                try:
                    result.append(level_sum / level_count)
                except :
                    pass
                level_sum = node.val
                level_count = 1
                cur_level = lv

            
        result.append(level_sum / level_count)
        
        return result
# @lc code=end

