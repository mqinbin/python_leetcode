#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除排序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        cur_num = nums[-1]
        count = 0
        for i in range(len(nums)-1, -1,-1):
            if nums[i] == cur_num:
                count += 1
            else:
                cur_num = nums[i]
                count = 1
            if count > 2:
                nums.pop(i)
        return len(nums)
# @lc code=end

