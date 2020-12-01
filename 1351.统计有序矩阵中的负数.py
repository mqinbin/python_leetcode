#
# @lc app=leetcode.cn id=1351 lang=python3
#
# [1351] 统计有序矩阵中的负数
#

# @lc code=start
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # answer = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] <0:
        #             answer += 1

        # return answer

        # rows = len(grid)
        # cols = len(grid[0])
        # row_index = rows-1
        # col_index = 0
        # answer = 0
        # while row_index >= 0 and col_index < cols:
        #     if grid[row_index][col_index]<0:
        #         answer += cols - col_index
        #         row_index -= 1
        #     else:
        #         col_index += 1
        # return answer

        def find_first_neg_index(arr,start,end):
            while start < end:
                mid = (start + end ) // 2
                if arr[mid] >= 0:
                    start = mid + 1
                else:
                    end = mid
            return start

        answer  = 0 
        start = 0
        end = len(grid[0])
        for arr in grid:
            end =  find_first_neg_index(arr, start, end)
            answer += len(grid[0]) - end

        return answer



# @lc code=end

