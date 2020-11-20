#
# @lc app=leetcode.cn id=1114 lang=python3
#
# [1114] 按序打印
#

# @lc code=start
from threading import Lock
class Foo:
    def __init__(self):
        pass
        self.lockA = Lock()
        self.lockB = Lock()
        self.lockC = Lock()
        self.lockB.acquire()
        self.lockC.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        self.lockA.acquire()
        printFirst()
        self.lockB.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        self.lockB.acquire()
        printSecond()
        self.lockC.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        self.lockC.acquire()
        printThird()
        self.lockA.release()
# @lc code=end

