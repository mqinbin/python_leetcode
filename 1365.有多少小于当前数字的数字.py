#
# @lc app=leetcode.cn id=1365 lang=python3
#
# [1365] 有多少小于当前数字的数字
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        dic = { }
        for index, num in enumerate(sorted_nums):
            if num not in dic:
                dic[num] = index
        return list(map(lambda num: dic[num] , nums))
# @lc code=end

