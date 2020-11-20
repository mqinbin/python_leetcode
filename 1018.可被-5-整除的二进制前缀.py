#
# @lc app=leetcode.cn id=1018 lang=python3
#
# [1018] 可被 5 整除的二进制前缀
#

# @lc code=start
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        cur = 0
        answer = []
        for bit in A:
            cur = (cur << 1) + bit
            answer.append( not cur % 5)
        return answer
# @lc code=end

