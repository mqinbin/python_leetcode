#
# @lc app=leetcode.cn id=1518 lang=python3
#
# [1518] 换酒问题
#

# @lc code=start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        fb = numBottles
        eb = 0
        answer = 0
        while fb:
            answer += fb
            eb += fb
            fb = eb // numExchange
            eb = eb % numExchange
        
        return answer

# @lc code=end

