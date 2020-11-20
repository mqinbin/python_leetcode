#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if target < nums[left] :
                left = mid + 1
                continue
            if target > nums[right - 1]:
            
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
# @lc code=end

