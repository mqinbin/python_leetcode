#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num ==0:
            return "0"
        elif num > 0:
            return self.convertPositiveToBase7(num)
        else:
            return "-" + self.convertPositiveToBase7(-num)
    def convertPositiveToBase7(self, num)->str:
        result = ""
        while num > 0:
            result =str( num % 7) + result
            num //= 7
        return result
        
# @lc code=end

