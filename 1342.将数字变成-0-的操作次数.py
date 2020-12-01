#
# @lc app=leetcode.cn id=1342 lang=python3
#
# [1342] 将数字变成 0 的操作次数
#

# @lc code=start
class Solution:
    def numberOfSteps (self, num: int) -> int:
        # answer = 0
        # while num:
        #     if num % 2 == 0:
        #         num >>= 1
        #     else:
        #         num -= 1
        #     answer += 1
        # return answer
        binstr = bin(num)[2:]
        return len(binstr) -1 + binstr.count('1')


# @lc code=end

