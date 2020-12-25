#
# @lc app=leetcode.cn id=201 lang=python3
#
# [201] 数字范围按位与
#

# @lc code=start
class Solution:
    # def rangeBitwiseAnd(self, m: int, n: int) -> int:
    #     answer =n
    #     for i in range(m,n):
    #         answer &= i

    #     return answer

    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        i = 0
        while m!=n:
            m >>= 1
            n >>= 1
            i += 1
        return n<<i
# @lc code=end

