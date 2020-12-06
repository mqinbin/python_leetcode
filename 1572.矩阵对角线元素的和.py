#
# @lc app=leetcode.cn id=1572 lang=python3
#
# [1572] 矩阵对角线元素的和
#

# @lc code=start
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)

        total = sum( mat[i][i] + mat[i][n-i-1] for i in range(n))
        total -= n%2 * mat[n//2][n//2]
        return total

# @lc code=end

