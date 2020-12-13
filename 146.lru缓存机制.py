#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#

# @lc code=start


class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity =capacity
        self.n = 0
        self.head =None
        self.data = {}

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        node = self.data[key]
        if node != self.head:
            self._dropNode(node)

            self._addToHead(node)
        return node.value


    def put(self, key: int, value: int) -> None:
        if self.head is None:
            node = Node(key,value)
            node.next = node
            node.pre = node
            self.head = node
            self.data[key] = node
            self.n = 1
            return 
        if key in self.data:
            node = self.data[key]
            node.value = value
            if node == self.head:
                return
            self._dropNode(node)
            self._addToHead(node)
            return

        node = Node(key,value)
        self._addToHead(node)
        self.data[key] = node
        self.n += 1

        if self.n > self.capacity:
            tail = self.head.pre
            self._dropNode(tail)

            del self.data[tail.key]
            self.n -= 1

    def _dropNode(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
    def _addToHead(self, node):
        node.next = self.head
        node.pre = self.head.pre
        self.head.pre.next = node
        self.head.pre = node
        self.head = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

