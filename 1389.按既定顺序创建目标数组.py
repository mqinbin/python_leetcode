#
# @lc app=leetcode.cn id=1389 lang=python3
#
# [1389] 按既定顺序创建目标数组
#

# @lc code=start
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        answer = []
        for num ,i in zip(nums, index):
            answer.insert(i,num)

        return answer
# @lc code=end

