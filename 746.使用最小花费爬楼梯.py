#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f0 = f1 = 0
        for c in cost:
            cur = min(f0,f1)+ c
            f1 = f0
            f0 = cur
        return min(f0,f1)

        
# @lc code=end

