#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return self.how_many_one(x^y)

    def how_many_one(self, n):
        result = 0
        while n > 0 :
            result +=  not ((n>>1 <<1) == n )
            n >>=1
        return result
# @lc code=end

