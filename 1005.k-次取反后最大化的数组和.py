#
# @lc app=leetcode.cn id=1005 lang=python3
#
# [1005] K 次取反后最大化的数组和
#

# @lc code=start
class Solution:
    # def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
    #     A.sort()
    #     j = 0
    #     for i in range(K):
    #         if A[j] < 0:
    #             A[j] *= -1
    #             j += 1
    #         elif A[j] > 0:
    #             if j-1>=0 and 0<=A[j-1]< A[j]:
    #                 A[j-1] *= -1
    #                 j -= 1
    #             else:
    #                 A[j] *= -1
    #         print(A)
    #     return sum(A)   
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        import heapq
        heapq.heapify(A)
        for _ in range(K):
            heapq.heappush(A ,- heapq.heappop(A))
        return sum(A) 
# @lc code=end

