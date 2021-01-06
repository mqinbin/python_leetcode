#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
            
        dic  = {}

        stack = [node]
        while stack:
            n = stack.pop()
            
            if not n or n in dic:
                continue
            else:
                if n.neighbors:
                    stack.extend(n.neighbors)
                dic[n] = Node(n.val)

        for key in dic:
            dic[key].neighbors = [dic[x] for x in key.neighbors] if key.neighbors else []
        


        return dic[node]


# @lc code=end
