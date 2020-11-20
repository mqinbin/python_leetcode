#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            else:
                nums[i], nums[i-zero_count] = nums[i-zero_count], nums[i]
        for i in range(zero_count):
            nums[-i-1] =0


# @lc code=end
