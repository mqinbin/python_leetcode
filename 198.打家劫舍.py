#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        nums.append(0)
        for i in range(len(nums) -4,-1,-1):
            nums[i] += max(nums[i+2],nums[i+3])

        return max(nums[:2])


    # def rob(self, nums: List[int]) -> int:
    #     if len(nums) == 0:
    #         return 0
    #     if len(nums) <= 2:
    #         return max(nums)
        
    #     return max( nums[0]+ self.rob(nums[2:]) , nums[1] + self.rob(nums[3:])  )

# @lc code=end

