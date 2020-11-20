#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
from typing import List
# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1

        max_area = 0
        while l < r:
            hl = height[l]
            hr = height[r]
            max_area = max(min(hl, hr) * (r-l), max_area)
            if hl <= hr:
                l += 1
            else:
                r -= 1

        return max_area

if __name__ == "__main__":
    n = Solution().maxArea([7,1,1,1,1,1,1,10,8])
    print(n)
# @lc code=end
