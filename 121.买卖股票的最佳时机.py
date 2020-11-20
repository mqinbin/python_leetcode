#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit = max(prices[i] - min_price ,max_profit)
            min_price = min(min_price, prices[i])
        return max_profit

# @lc code=end

