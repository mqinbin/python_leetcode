#
# @lc app=leetcode.cn id=405 lang=python3
#
# [405] 数字转换为十六进制数
#

# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:
        table = '0123456789abcdef'
        if num <0:
            num = 0x100000000 + num
        result = ""
        while num:
            num, m = divmod(num,16)
            result =  table[m] + result
        return result if result else "0"
# @lc code=end

