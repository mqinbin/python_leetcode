#
# @lc app=leetcode.cn id=1413 lang=python3
#
# [1413] 逐步求和得到正数的最小值
#

# @lc code=start
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        glide_sum = 0
        target = glide_sum
        for num in nums:
            glide_sum += num
            target = min(glide_sum,target)

        return max(1, -target+1)

# @lc code=end

