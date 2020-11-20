#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
import operator
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x>=0 else -1
        result = int(str(sign * x)[::-1])
        return result * sign if result < 2**31 else 0
# @lc code=end

