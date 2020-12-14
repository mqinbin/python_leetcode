#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    # dp 分治
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        leftAnswer =  self.maxSubArray(nums[:n//2])
        rightAnswer =  self.maxSubArray(nums[n//2:n])

        midLPart,midRPart = nums[n//2-1],nums[n//2]

        temp = 0
        for i in range(n//2-1 , -1 ,-1):
            temp += nums[i]
            midLPart = max(midLPart,temp)
        temp = 0
        for i in range(n//2,n):
            temp += nums[i]
            midRPart = max(midRPart,temp)
        return max(midLPart+midRPart,leftAnswer,rightAnswer)

    # dp
    # def maxSubArray(self, nums: List[int]) -> int:
    #     # [-2,1,-3,4,-1,2,1,-5,4]
    #     n = len(nums)
    #     if n < 1:
    #         return 0
    #     answer = nums[0]
    #     for i in range(1,n):
    #         nums[i] += max(0,nums[i-1])
    #         answer = max(answer,nums[i])
    #     return answer

# @lc code=end

