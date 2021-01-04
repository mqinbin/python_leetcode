#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#

# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def aroundLives(board, i,j):
            n = len(board)
            m = len(board[0])
            answer = 0
            for line in range(max(0,i-1) , min(i+1,n)):
                for row in range(max(0,j-1) , min(j+1,m)):
                    if line != i  and row != j  and board[line][row] == 1:
                        answer += 1
            return answer
# @lc code=end

