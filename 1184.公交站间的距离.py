#
# @lc app=leetcode.cn id=1184 lang=python3
#
# [1184] 公交站间的距离
#

# @lc code=start
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total = sum(distance)
        small = min(start,destination)
        large = max(start,destination)
        part = sum(distance[small:large])
        return min(part, total-part)
# @lc code=end

