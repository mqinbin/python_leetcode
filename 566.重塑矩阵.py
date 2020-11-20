#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#

# @lc code=start
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(nums) * len(nums[0]):
            return nums
        
        from itertools import chain
        result = []
        count = 0
        temp = []
        for e in chain(*nums):
            count+=1
            temp.append(e)
            if count == c:
                result.append(temp)
                temp = []
                count = 0
        return result
# @lc code=end

