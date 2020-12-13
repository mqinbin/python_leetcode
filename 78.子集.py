#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        answer = []

        for k in range(0,len(nums) + 1):
            answer.extend(list(combinations(nums,k)))
        return answer
# @lc code=end

