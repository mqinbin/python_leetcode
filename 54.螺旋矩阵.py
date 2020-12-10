#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        return matrix.pop(0) + self.spiralOrder( list(map(list,zip(*matrix)))[::-1] )
          



# @lc code=end

