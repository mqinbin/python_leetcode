#
# @lc app=leetcode.cn id=1051 lang=python3
#
# [1051] 高度检查器
#

# @lc code=start
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        answer = 0
        for t in zip(heights,sorted(heights)):
            if t[0] != t[1]:
                answer += 1
        return answer
# @lc code=end

