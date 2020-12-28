#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return sorted(nums)[-k]
        import heapq
        heap = [float("-inf")] * k
        for num in nums:
            if num >= heap[0]:
                heapq.heappushpop(heap,num)

        return heap[0]
# @lc code=end

