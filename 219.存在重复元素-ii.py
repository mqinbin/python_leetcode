#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cache = {}
        for i, num in enumerate(nums):
            if num in cache and i - cache[num] <= k:
                return True
            cache[num] = i
        
        return False


# @lc code=end

