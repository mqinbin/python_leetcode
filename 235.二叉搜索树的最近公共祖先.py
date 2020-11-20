#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def find_path(self, root, node):
        result = []
        cur = root
        while True:
            result.append(cur)
            if cur.val == node.val:
                break
            if cur.val < node.val:
                cur = cur.right
            else:
                cur =cur.left 
        return result

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = self.find_path(root, p)        
        q_path = self.find_path(root, q)
        print(len(p_path))
        print(len(q_path))

        for i in range(min(len(p_path) ,len(q_path))):
            if p_path[i].val != q_path[i].val:
                break
        else:
            return p_path[i]
        return p_path[i-1]




# @lc code=end

