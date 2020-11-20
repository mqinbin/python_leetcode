#
# @lc app=leetcode.cn id=762 lang=python3
#
# [762] 二进制表示中质数个计算置位
#

# @lc code=start
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        primarys = set([2,3,5,7,11,13,17,19])

        answer = 0
        for n in range(L,R+1):
            if self.one_count(n) in primarys:
                answer +=1
        
        return answer

    def one_count(self, n):
        return bin(n).count('1')
# @lc code=end

