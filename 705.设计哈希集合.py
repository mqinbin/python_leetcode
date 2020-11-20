#
# @lc app=leetcode.cn id=705 lang=python3
#
# [705] 设计哈希集合
#

# @lc code=start


class MyHashSet:
    def __init__(self , size = 16):
        self.data = 0

    def add(self, key: int) -> None:
        self.data |= 1<<key


    def remove(self, key: int) -> None:
        if self.contains(key):
            self.data ^= (1<<key)


    def contains(self, key: int) -> bool:

        return bool(self.data & (1<<key) )

"""
class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    # def __repr__(self):
    #     result = ""
    #     result += str(self.val)
    #     if self.next:
    #         result += "->" + str(self.next)
    #     return result

class MyHashSet:

    def __init__(self , size = 16):

        self.n = 0
        self.cap = 16
        self.data = [None] * size
        self.fact = 0.75

    def hash(self, val):
        return (val +  self.cap) % self.cap


    def resize(self,new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        self.cap = new_cap

        for cell in old_data:
            if cell :
                cur = cell
                while cur:
                    self.add(cur.val)
                    cur = cur.next
        del old_data

    def add(self, key: int) -> None:
        if self.n == self.cap * self.fact:
            self.resize( self.cap * 2)
        
        data = self.data

        cell = data[self.hash(key)]
        if cell:
            cur = cell
            while cur:
                if cur.val == key:
                    return
                cur = cur.next
            self.n += 1
            data[self.hash(key)] =  LinkNode(key)
            data[self.hash(key)].next= cell
            return 
        else:
            data[self.hash(key)] = LinkNode(key)
            self.n += 1
            return


    def remove(self, key: int) -> None:

        data = self.data

        print(key, data)

        cell = data[self.hash(key)]
        if cell:
            if cell.val == key:
                data[self.hash(key)] = cell.next
                self.n -= 1
                return 
            cur = cell
            while cur:
                if cur.next and cur.next.val == key:
                    cur.next = cur.next.next
                    self.n -=1
                    break
                cur = cur.next
            return
        else:
            return


    def contains(self, key: int) -> bool:
        data = self.data
        cell = data[self.hash(key)]
        if cell:
            cur = cell
            while cur:
                if cur.val == key:
                    return True
                cur = cur.next
            return False
        else:
            return False
"""

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

