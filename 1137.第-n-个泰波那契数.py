#
# @lc app=leetcode.cn id=1137 lang=python3
#
# [1137] 第 N 个泰波那契数
#

# @lc code=start
cache = [0,1,1]
class Solution:
    def tribonacci(self, n: int) -> int:
        global cache 
        index = n
        window_sum = sum(cache[-3:])
        while len(cache) -1 < index  :
            
            cache.append(window_sum)
            window_sum += window_sum - cache[-4]

        return cache[n]

# @lc code=end

