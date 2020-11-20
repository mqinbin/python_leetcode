#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心索引
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        
        first_half = 0
        for i in range(len(nums)):
            if total - first_half - nums[i] == first_half:
                return i
            first_half += nums[i]

        return -1

# @lc code=end

