#
# @lc app=leetcode.cn id=1374 lang=python3
#
# [1374] 生成每种字符都是奇数个的字符串
#

# @lc code=start
class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 ==0:
            return "a" + "b" * (n-1)
        else:
            return "a" * n
# @lc code=end

