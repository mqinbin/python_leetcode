#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for offset in range(32):
            if n & (1<<offset) !=0:
                result |= 1 <<(31-offset)
        return result

        
# @lc code=end

