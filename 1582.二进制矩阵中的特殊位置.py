#
# @lc app=leetcode.cn id=1582 lang=python3
#
# [1582] 二进制矩阵中的特殊位置
#

# @lc code=start
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_sum = [sum(x) for x in mat]
        col_sum = [sum(x) for x in zip(*mat)]

        return sum([ mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1
        for i in range(len(mat))
        for j in range(len(mat[0]))
        ])
# @lc code=end

