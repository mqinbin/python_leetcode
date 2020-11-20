#
# @lc app=leetcode.cn id=507 lang=python3
#
# [507] 完美数
#

# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <2:
            return False
        
        result = 1
        for f in range(2, int(num**0.5) + 1):
            if num % f == 0:
                result += f
                if num != f * f:
                    result += num // f
        return result == num 

# @lc code=end

