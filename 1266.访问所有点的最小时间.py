#
# @lc app=leetcode.cn id=1266 lang=python3
#
# [1266] 访问所有点的最小时间
#

# @lc code=start
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        answer = 0
        for i in range(1, len(points)):
            answer += max( abs(points[i][0]  - points[i-1][0] ) ,abs(points[i][1]  - points[i-1][1] ) )

        return answer
# @lc code=end

