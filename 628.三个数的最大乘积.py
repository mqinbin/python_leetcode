#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#

# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()


        if nums[-1] > 0:
            if nums[0] * nums[1] > nums[-3] * nums[-2]:
                return nums[0] * nums[1] * nums[-1]
            else:
                return nums[-3] * nums[-2] * nums[-1]
        elif nums[-1] == 0:
            return 0
        else:
            return nums[-3] * nums[-2] * nums[-1]

        
# @lc code=end

