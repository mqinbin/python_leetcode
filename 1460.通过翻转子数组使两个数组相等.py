#
# @lc app=leetcode.cn id=1460 lang=python3
#
# [1460] 通过翻转子数组使两个数组相等
#

# @lc code=start
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        from collections import Counter
        return Counter(target) == Counter(arr)
# @lc code=end

