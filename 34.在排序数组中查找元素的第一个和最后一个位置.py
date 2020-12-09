#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left ,right = 0,len(nums)
        found = -1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                found = mid
                break
            if target>nums[mid]:
                left = mid + 1
            else:
                right = mid
        if found == -1:
            return [-1,-1]
        answer = [0,len(nums)-1]
        for i in range(found-1,-1,-1):
            if nums[i] != nums[found]:
                answer[0] = i+1
                break
        for i in range(found+1,len(nums)):
            if nums[i] != nums[found]:
                answer[1] = i-1
                break
        return answer
# @lc code=end

