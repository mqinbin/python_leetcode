#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        answer = []
        deque = [root]
        temp = []
        target = 1
        nones = 0
        while deque:
            cur = deque.pop(0)
            temp.append(cur.val)
            if cur.left:
                deque.append(cur.left)
            else:
                nones += 1
            if cur.right:
                deque.append(cur.right)
            else:
                nones += 1
            if len(temp)  == target:
                answer.append(temp)
                temp =[]
                target = target * 2 - nones
                nones = 0
        if temp:
            answer.append(temp)
        return answer
# @lc code=end

