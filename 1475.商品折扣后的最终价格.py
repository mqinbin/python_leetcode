#
# @lc app=leetcode.cn id=1475 lang=python3
#
# [1475] 商品折扣后的最终价格
#

# @lc code=start
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = prices[:]
        stack = [] # 存放index
        for i in range(len(prices)):
            while stack and prices[i]<=prices[stack[-1]]:
                pop_index =stack.pop()
                answer[pop_index] -= prices[i]

            stack.append(i)

        return answer

# @lc code=end

