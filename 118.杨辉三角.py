#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        result = [[1]]
        for i in range(1, numRows):
            result.append([])
            result[-1].append(1)
            for j in range(1,i):
                result[-1].append(result[-2][j-1]  + result[-2][j] )
            result[-1].append(1)
        return result
# @lc code=end

