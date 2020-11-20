#
# @lc app=leetcode.cn id=1046 lang=python3
#
# [1046] 最后一块石头的重量
#

# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        nstones =[-x for x in stones]
        heapq.heapify(nstones)
        while len(nstones) > 1:
            first = heapq.heappop(nstones)
            second = heapq.heappop(nstones)
            if first != second:
                heapq.heappush(nstones,first-second)
        if len(nstones) == 0:
            return 0
        else:
            return - nstones[0]


        
# @lc code=end

