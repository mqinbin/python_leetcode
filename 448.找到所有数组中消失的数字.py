#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            change_index = abs(nums[i] )-1
            nums[change_index] = - abs(nums[change_index] )

        result = []
        for i in range(len(nums)):
            if nums[i]> 0:
                result.append(i+1)
        return result

# @lc code=end

