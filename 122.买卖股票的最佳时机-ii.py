#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        prices.append(0)
        amount = 0
        # [7,1,5,3,6,4]
        for price in prices:
            if stack and price < stack[-1]:
                if len(stack) >=2:
                    amount += stack[-1] - stack[0]
                stack.clear()
            stack.append(price)
        return amount
# @lc code=end

