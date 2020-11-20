#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        value = nums[0]
        index = 1
        while index < len(nums):
            if value == nums[index]:
                del nums[index]
            else:
                value = nums[index]
                index +=1
        return len(nums)
# @lc code=end

