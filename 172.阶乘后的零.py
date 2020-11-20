#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        five_factor_count = sum( [ self.has_n_factor(m,5) for m in range(2,n+1)])
        # two_factor_count = sum( [ self.has_n_factor(m,2) for m in range(2,n+1)])
        # return min(five_factor_count , two_factor_count)
        return five_factor_count

    def has_n_factor(self, num, factor):
        result = 0
        while num >0 and num % factor == 0:
            num //= factor
            result +=1
        return result
# @lc code=end

