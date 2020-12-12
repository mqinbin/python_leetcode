#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_pos = []
        m = len(matrix)
        n = len(matrix[0])
        zero_rows = set()
        zero_cols = set()
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)
        
        for r in  zero_rows:
            for c in range(n):
                matrix[r][c] = 0
        for c in  zero_cols:
            for r in range(m):
                matrix[r][c] = 0       

# @lc code=end

