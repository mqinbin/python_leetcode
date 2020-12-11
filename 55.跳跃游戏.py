#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True
        
        cur_pow = nums[0]
        index = 1
        while cur_pow > 0  and index < len(nums):
            cur_pow -= 1
            if nums[index] > cur_pow:
                cur_pow = nums[index]
            index +=1
        return index == len(nums)
# @lc code=end

