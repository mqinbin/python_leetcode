#
# @lc app=leetcode.cn id=766 lang=python3
#
# [766] 托普利茨矩阵
#

# @lc code=start
from collections import deque
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        queue = deque(matrix[0])
        for r in range(1, len(matrix)):
            queue.pop()
            queue.append(matrix[r][0])
            for c in range(1,len(matrix[r])):
                if queue.popleft() != matrix[r][c]:
                    return False
                queue.append(matrix[r][c])
        
        return True

# @lc code=end

