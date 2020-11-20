#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0

        result = []

        for i in range(1, n-1):
            left_max = max(height[:i])
            right_max = max(height[i+1:])
            result.append(max(min(left_max, right_max) - height[i], 0))

        return sum(result)


# @lc code=end
