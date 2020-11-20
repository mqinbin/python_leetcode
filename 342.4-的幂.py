#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        # if num<=0:
        #     return False
        # if num & (num-1) == 0:
        #     return num & 0x55555555
        # return False
        return num > 0 and num & (num-1) == 0 and num & 0x55555555
# @lc code=end

