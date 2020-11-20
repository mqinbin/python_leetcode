#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, N: int) -> int:
        result = [ 0,1]
        for i in range(2, N +1):
            result.append(result[-2] + result[-1])
        
        return result[N]
        
# @lc code=end

