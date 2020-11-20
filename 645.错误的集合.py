#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = [0,0]
        for i in range(len(nums)):
            ci = abs(nums[i]) - 1
            if nums[ci] < 0:
                result[0] = ci + 1
            else:
                nums[ci] = - abs(nums[ci])

        for i in range(len(nums)):
            if nums[i] > 0:
                result[1] =i+1
                break
        
        return result


# @lc code=end

