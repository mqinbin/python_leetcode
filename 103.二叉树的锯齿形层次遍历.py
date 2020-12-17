#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        answer = []

        target = 1
        nones = 0
        deque = [root]
        from_left_to_right  = False
        temp = []
        while deque:
            node = deque.pop(0)
            temp.append(node.val)

            for child in ([node.left,node.right] ):
                if child:
                    deque.append(child)
                else:
                    nones += 1


            if len(temp) == target:
                if  from_left_to_right:
                    temp.reverse()
                answer.append(temp)
                temp = []
                target = target * 2 - nones
                nones = 0
                from_left_to_right = not from_left_to_right

        if temp:
            answer.append(temp)
            temp = []
        return answer





# @lc code=end

