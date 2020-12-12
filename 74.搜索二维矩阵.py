#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        up ,down ,left,right = 0,m,0,n

        row_found =-1
        while up < down:
            mid = (up + down ) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row_found = mid
                break
            if matrix[mid][0] > target:
                down = mid
                continue
            if matrix[mid][-1] < target:
                up = mid + 1
                continue
            print(up,",",down)
        if row_found == -1:
            return False
        
        while left < right:
            mid = (left+right) // 2
            if matrix[row_found][mid] > target:
                right = mid
                continue
            if matrix[row_found][mid]< target:
                left = mid + 1
                continue
            return True
        return False





        


# @lc code=end

