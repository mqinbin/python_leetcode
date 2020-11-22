#
# @lc app=leetcode.cn id=1287 lang=python3
#
# [1287] 有序数组中出现次数超过25%的元素
#

# @lc code=start
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        times = 0
        last =float('-inf')
        for num in arr:
            if num != last:
                times = 1
                last = num
            else:
                times += 1
            if times > n /4:
                return last
        return None

# @lc code=end

