#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        digits[n-1]+=1
        for i in range(n-1, 0, -1):
            if digits[i] >= 10:
                digits[i-1] +=1
                digits[i] -=10
        if digits[0] >= 10:
            digits[0] -=10
            digits = [1] + digits
        
        return digits

# @lc code=end

