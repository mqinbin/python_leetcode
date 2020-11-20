#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
import re
class Solution:
    def removeDuplicates(self, S: str) -> str:
        lefts = []
        for char in S:
            if lefts and char == lefts[-1]:
                lefts.pop()
            else:
                lefts.append(char)
        return "".join(lefts)
# @lc code=end

