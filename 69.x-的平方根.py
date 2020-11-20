#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
import math
class Solution:
    # def mySqrt(self, x: int) -> int:
    #     return math.floor(x ** 0.5) 
    def mySqrt(self, x: int) -> int:
        left , right = 0,x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x < (mid+1) * (mid+1):
                return mid
            if mid * mid > x:
                right = mid 
            else:
                left = mid+1

if __name__ == "__main__":
    print(Solution().mySqrt(1))
    print(Solution().mySqrt(2))
    print(Solution().mySqrt(4))
    print(Solution().mySqrt(5))
# @lc code=end

