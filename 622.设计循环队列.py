#
# @lc app=leetcode.cn id=622 lang=python3
#
# [622] 设计循环队列
#

# @lc code=start
class MyCircularQueue:

    def __init__(self, k: int):
        self.data = [None] * k
        self.start_idx = 0
        self.size = 0
        self.capicity = k
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.data[(self.start_idx + self.size) % self.capicity] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.data[self.start_idx] = None
        self.start_idx = (self.start_idx + 1) % self.capicity
        self.size -= 1
        return True



    def Front(self) -> int:
        if  self.isEmpty():
            return -1
        return self.data[self.start_idx]
        

    def Rear(self) -> int:
        if  self.isEmpty():
            return -1
        return self.data[(self.start_idx + self.size -1) % self.capicity ]
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.capicity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end

