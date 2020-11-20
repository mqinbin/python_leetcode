#
# @lc app=leetcode.cn id=693 lang=python3
#
# [693] 交替位二进制数
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        last_bit = -1
        while n:
            _mod = n % 2
            if last_bit == -1:
                last_bit = _mod
            elif _mod == last_bit:
                return False
            else:
                last_bit = _mod
            n //= 2
        return True
# @lc code=end

