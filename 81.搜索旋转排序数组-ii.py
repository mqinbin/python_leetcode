#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left , right = 0 , len(nums)
        while left < right:
            rotatePos = (left + right) // 2
            if rotatePos == len(nums) - 1:
                break
            if nums[rotatePos]>nums[rotatePos+1]:
                rotatePos += 1
                break
            if nums[rotatePos]>nums[left]:
                left = rotatePos + 1
            else:
                right = rotatePos
        
        def foundIndex(nums, left, right,target):
            while left < right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                if target>nums[mid]:
                    left = mid + 1
                else:
                    right = mid
            return -1
        
        leftPart = foundIndex(nums,0,rotatePos,target)
        if leftPart != -1:
            return True
        rightPart = foundIndex(nums,rotatePos,len(nums),target)
        return leftPart != -1
        
# @lc code=end

