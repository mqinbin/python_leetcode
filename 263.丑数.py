#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 1:
            return True
        
        for p in (2,3,5):
            while num > 0 and num % p == 0:
                num //= p
        return num == 1
# @lc code=end

