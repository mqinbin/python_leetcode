#
# @lc app=leetcode.cn id=706 lang=python3
#
# [706] 设计哈希映射
#

# @lc code=start



class LinkNode:
    def __init__(self, key,value):
        self.key = key
        self.next = None
        self.value = value

    def __repr__(self):
        result = ""
        result += "%d:%d" %(self.key,self.value)
        if self.next:
            result += "->" + str(self.next)
        return result

class MyHashMap:

    def __init__(self , size = 1600):

        self.n = 0
        self.cap = size
        self.data = [None] * size
        self.fact = 0.75

    def put(self, key: int, value: int) -> None:
        if self.n == self.cap * self.fact:
            self.resize( self.cap * 2)
        
        data = self.data

        cell = data[self.hash(key)]
        if cell:
            cur = cell
            while cur:
                if cur.key == key:
                    cur.value =value
                    return
                cur = cur.next
            self.n += 1
            data[self.hash(key)] =  LinkNode(key,value)
            data[self.hash(key)].next= cell
            return 
        else:
            data[self.hash(key)] = LinkNode(key,value)
            self.n += 1
            return
        

    def get(self, key: int) -> int:
        data = self.data
        cell = data[self.hash(key)]
        if cell:
            cur = cell
            while cur:
                if cur.key == key:
                    return cur.value
                cur = cur.next
            return -1
        else:
            return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        data = self.data


        cell = data[self.hash(key)]
        if cell:
            if cell.key == key:
                data[self.hash(key)] = cell.next
                self.n -= 1
                return 
            cur = cell
            while cur:
                if cur.next and cur.next.key == key:
                    cur.next = cur.next.next
                    self.n -=1
                    break
                cur = cur.next
            return
        else:
            return

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
                    self.put(cur.key,cur.value)
                    cur = cur.next
        del old_data

        



        



    
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

