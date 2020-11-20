#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#

# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        s = set()
        for i in range(0, int(c ** 0.5)  + 1):
            s.add(i*i)

        for e in s:
            if c-e in s:
                return True
        return False
# @lc code=end

