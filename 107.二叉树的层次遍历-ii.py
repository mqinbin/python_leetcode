#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = {}
        self.traval_deepth(root,0,result)
        levels = sorted(result.keys(),reverse = True)
        return [result[lv] for lv  in levels]

    def traval_deepth(self, node, level, data):
        if not node:
            return
        if level not in data:
            data[level] = []
        if node:
            data[level].append(node.val)
        self.traval_deepth(node.left,level+1,data)
        self.traval_deepth(node.right,level+1,data)
        


    
    



# @lc code=end

