#
# @lc app=leetcode.cn id=1486 lang=python3
#
# [1486] 数组异或操作
#

# @lc code=start
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        answer = 0
        for i in range(n):
            answer ^= start + i * 2
        return answer
# @lc code=end

