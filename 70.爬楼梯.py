#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=3:
            return n

        cache = [1,2,3]
        
        i = 3
        while i < n:
            cache.append(cache[i-1] + cache[i-2])
            i+=1
        
        return cache[-1]


# @lc code=end

