#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start


class Solution:

    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        result = [True] * n
        result[0] =result[1] =False

        for i in range(2,n):
            if result[i]:
                for j in range(i*i , n , i):
                    result[j] = False

        return sum(result) 


# @lc code=end

