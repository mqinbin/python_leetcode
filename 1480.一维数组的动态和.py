#
# @lc app=leetcode.cn id=1480 lang=python3
#
# [1480] 一维数组的动态和
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        answer = []
        for num in nums:
            total +=num
            answer.append(total)
        return answer

# @lc code=end

