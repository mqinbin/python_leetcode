#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        result = 0
        for _ in range(1, 0xffffffff,2):
            result += _
            if num == result:
                return True
            if result > num:
                return False
                
# @lc code=end

