#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def a(down,up):
            answer = 1
            for i in range(up):
                answer *= down - i
            return answer
        def c(down,up):
            return a(down,up) // a(up,up)
        m ,n = m-1,n-1
        return c(m+n,min(m,n))

# @lc code=end

