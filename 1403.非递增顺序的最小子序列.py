#
# @lc app=leetcode.cn id=1403 lang=python3
#
# [1403] 非递增顺序的最小子序列
#

# @lc code=start
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        import heapq
        heap = []
        total = 0
        for num in nums:
            total += num
            heapq.heappush(heap,-num)
        import math
        half = math.ceil(total / 2)
        answer = []
        while heap:
            top = heapq.heappop(heap)
            total += top
            answer.append(-top)
            if total < half:
                break
        return answer
# @lc code=end

