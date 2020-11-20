#
# @lc app=leetcode.cn id=441 lang=python3
#
# [441] 排列硬币
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        for k in range(1,2**32):
            if n < k * (k + 1) // 2:
                return k-1
        
# @lc code=end

