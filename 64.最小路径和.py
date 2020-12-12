#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        temp = 0
        helper = [float('inf')]
        for num in grid[0]:
            temp += num
            helper.append(temp)

        for r in range(1,rows):
            for c in range(1,cols+1):
                helper[c] = grid[r][c-1] + min(helper[c],helper[c-1])
            # print(helper)
        return helper[-1]
# @lc code=end

