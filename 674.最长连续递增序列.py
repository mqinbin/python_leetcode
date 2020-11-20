#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:

        answer = bool(nums) - 0
        l = 0

        for r in range(1, len(nums)):
            if nums[r] > nums[r-1]:
                answer = max(answer, r-l + 1)
            else:
                l = r
        return answer
# @lc code=end

