#
# @lc app=leetcode.cn id=1217 lang=python3
#
# [1217] 玩筹码
#

# @lc code=start
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        answer = [0,0]
        for p in position:
            answer[p%2] += 1
        return min(answer)
# @lc code=end

