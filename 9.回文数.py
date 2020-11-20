#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        range  = 1
        while x // range >=10:
            range *=10
        while x:
            left = x // range
            right = x % 10
            if left != right:
                return False
            
            x = (x%range) //10
            range //= 100
        return True
# @lc code=end

