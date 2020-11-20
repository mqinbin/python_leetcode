#
# @lc app=leetcode.cn id=728 lang=python3
#
# [728] 自除数
#

# @lc code=start
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [ x for x in range(left, right+1) if self.isSelfDividingNumbers(x)]
    
    def isSelfDividingNumbers(self,num):
        temp = num
        while temp>0:
            mod = temp % 10
            if mod == 0:
                return False
            if num % mod == 0 :
                temp //=10
            else:
                return False
        return True
# @lc code=end

