#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = [[] for _ in range(numRows)]
        offset = 1
        start = 0
        for char in s:
            result[start].append(char)
            if numRows == 1:
                offset = 0
            elif start == numRows -1:
                offset = -1
            elif start == 0:
                offset = 1
            start += offset
        from itertools import chain
        return "".join(chain(*result))


# @lc code=end

