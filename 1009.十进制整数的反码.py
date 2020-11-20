#
# @lc app=leetcode.cn id=1009 lang=python3
#
# [1009] 十进制整数的反码
#

# @lc code=start
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        def bitCount(n):
            answer = 0
            while n>0:
                n >>= 1
                answer+=1
            return answer

        return N ^ ((1 << bitCount(N))- 1)
# @lc code=end

