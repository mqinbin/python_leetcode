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

    # 字典
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic = {}
        node = head
        while node:
            dic[node] = Node(node.val)
            node = node.next
        node = head
        while node:
            dic[node].next = dic[node.next] if node.next else None
            dic[node].random = dic[node.random] if node.random else None
            node = node.next
        return dic[head] if head  else None



    # 连续链表
    # def copyRandomList(self, head: 'Node') -> 'Node':

    #     node = head
    #     while node:
    #         temp = node.next
    #         newNode = Node(node.val, temp)
    #         node.next = newNode
    #         node = node.next.next

    #     node = head
    #     while node:
    #         node.next.random = node.random.next if node.random else None
    #         node = node.next.next
        
    #     dummy = Node(0)
    #     cloneNode = dummy
    #     node = head
    #     while node:
    #         cloneNode.next  = node.next
    #         cloneNode = node.next
    #         node.next = cloneNode.next
    #         node = node.next


    #     return dummy.next


# @lc code=end

