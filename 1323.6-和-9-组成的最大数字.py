#
# @lc app=leetcode.cn id=1323 lang=python3
#
# [1323] 6 和 9 组成的最大数字
#

# @lc code=start
class Solution:
    def maximum69Number (self, num: int) -> int:
        # num = str(num)
        # answer = ""
        # found = False
        # for char in num:
        #     if not found and char == "6":
        #         char = "9"
        #         found = True
        #     answer += char
        # return int(answer)
        return int(str(num).replace('6','9',1))
# @lc code=end

