#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start

from typing import List
def enqueue(l:List,val):
    l.append(val)

def dequeue(l):
    result = l[0]
    del l[0]
    return result

def peek(l):
    return l[0]

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 =[]
        self.q2 =[]


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self.q1:
            enqueue(self.q2,x)
            while self.q1:
                enqueue(self.q2, dequeue(self.q1))
            self.q1 , self.q2 = self.q2 , self.q1
        else:
            enqueue(self.q1,x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return dequeue(self.q1)


    def top(self) -> int:
        """
        Get the top element.
        """
        return peek(self.q1)

    def empty(self) -> bool:
        return not (self.q1 or self.q2)



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

