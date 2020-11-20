#
# @lc app=leetcode.cn id=1089 lang=python3
#
# [1089] 复写零
#

# @lc code=start
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        pos = 0
        while pos < len(arr):
            if arr[pos] == 0:
                arr.pop()
                arr.insert(pos,0)
                pos += 2
            else:
                pos += 1
        
# @lc code=end

