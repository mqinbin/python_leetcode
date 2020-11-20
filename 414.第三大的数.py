#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max_heap = [float('-inf')] * 3

        for num in nums:
            if num > max_heap[0]:
                max_heap = [num,max_heap[0],max_heap[1]]
                continue
            if num < max_heap[0] and  num > max_heap[1]:
                max_heap = [max_heap[0],num,max_heap[1]]
                continue
            if  num < max_heap[1] and num > max_heap[2]:
                max_heap = [max_heap[0],max_heap[1] ,num]
        
        # for i in range(2,-1,-1):
        #     if max_heap[i] != float('-inf'):
        #         return max_heap[i]
        return max_heap[2] if max_heap[2] != float('-inf') else  max_heap[0]
                

        
# @lc code=end

