#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result  = sum(nums[0:k])
        cur = result 
        for i in range(1, len(nums) - k + 1):
            cur += (nums[i-1+k] - nums[i-1] )
            result = max(result, cur)
        
        return result / k

        
# @lc code=end

