#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def quickPow(x , n):
            if n == 0:
                return 1
            y = quickPow(x,n//2)
            return y * y * (x if n%2 else 1)

        flag = n > 0
        answer = quickPow(x , abs(n))
        return answer if flag else 1/answer


# @lc code=end

