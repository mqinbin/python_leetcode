#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle) 
        dp = [0] * (n + 1)
        for i in range (n-1,-1,-1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j] , dp[j+1])
        return dp[0]

# @lc code=end

