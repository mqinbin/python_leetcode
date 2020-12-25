#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        l = []
        cur = head
        while cur:
            l.append[Node(cur.val)]
            cur = cur.next
        
        cur = head
        n = len(l)
        for i in range(n):
            l[i].next = None if  i == n-1 else l[i+1]
            l[i].random = cur.random

            cur = cur.next
        
# @lc code=end

