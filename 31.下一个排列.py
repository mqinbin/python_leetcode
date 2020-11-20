#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        stack = []
        right = len(nums) - 1
        left = 0
        # [1,3,2]
        # i 1  left 1  right 2
        for i in range(right, 0, -1):
            if nums[i] > nums[i-1]:
                left = i
                break
        
        if left > 0:
            for j in range(right, left-1, -1):
                if nums[j] > nums[left-1]:
                    nums[j], nums[left-1] = nums[left-1], nums[j]
                    break
        while left < right :
            nums[left], nums[right] = nums[right], nums[left]
            left +=1
            right -=1
        return


# @lc code=end
