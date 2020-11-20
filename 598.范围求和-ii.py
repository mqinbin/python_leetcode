#
# @lc app=leetcode.cn id=598 lang=python3
#
# [598] 范围求和 II
#

# @lc code=start
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        minc = minr = 2**31
        for op in ops:
            minc = min(op[0],minc)
            minr = min(op[1],minr)
        if minc == minr == 2**31:
            return m * n
        else:
            return minc * minr
# @lc code=end

