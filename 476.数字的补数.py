#
# @lc app=leetcode.cn id=476 lang=python3
#
# [476] 数字的补数
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        bits = self.count_bits(num) 
        return ((1 << bits ) - 1) ^ num
    def count_bits(self,n):
        result = 0
        while n>0:
            n>>=1
            result+=1
        return result

# @lc code=end

