#
# @lc app=leetcode.cn id=1252 lang=python3
#
# [1252] 奇数值单元格的数目
#

# @lc code=start
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        answer = [[0 for _ in range(m)] for _ in range(n)  ]
        print(answer)

        def incre( row , col):
            for x in range(m):
                answer[row][x] += 1
            for y in range(n):
                answer[y][col] += 1

            
        
        for index in indices:
            incre(*index)
        
        return sum([answer[r][c]&1 for r in range(n) for c in range(m)])
# @lc code=end

