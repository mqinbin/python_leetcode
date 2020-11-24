#
# @lc app=leetcode.cn id=1317 lang=python3
#
# [1317] 将整数转换为两个无零整数的和
#

# @lc code=start
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def contains_zero(num):
            if num == 0 :
                return True
            if num % 10 == 0:
                return True
            num //= 10
            if num == 0:
                return False
            else:
                return contains_zero(num)
        
        for i in range(1, n ):
            if not contains_zero(i) and not contains_zero(n-i):
                return [i,n-i]
        
# @lc code=end

