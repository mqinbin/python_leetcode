#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
        else:
            if self.min_stack[-1] >= x:
                self.min_stack.append(x)

    def pop(self) -> None:
        x = self.data.pop()
        if x == self.min_stack[-1] :
            self.min_stack.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

