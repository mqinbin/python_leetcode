#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        helper = [0] * (cols + 1)
        
        if obstacleGrid[0][0]:
            return 0
        helper[1] = 1   
        for r in range(rows):
            for c in range(1,cols+1):
                if obstacleGrid[r][c-1] == 1:
                    helper[c] = 0
                else:
                    helper[c] += helper[c-1] 
        return helper[cols]
# @lc code=end

