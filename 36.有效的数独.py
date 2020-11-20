#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(0,9):
            rnums = self.get_row(board,i,0)
            if len(rnums) != len(set(rnums)):
                return False

            cnums = self.get_col(board,0,i)
            if len(cnums) != len(set(cnums)):
                return False

        for i in range(3):
            for j in range(3):
                bnums = self.get_cell(board, i*3,j*3)
                if len(bnums) != len(set(bnums)):
                    return False
        return True

    def get_row(self, board ,r, c):
        return [x for x in board[r] if x != "." ]
    def get_col(self, board, r,c):
        return [board[x][c] for x in range(9) if board[x][c] != "." ]
    def get_cell(self, board, r,c):
        rb = r // 3
        cb = c // 3
        return  [ board[i][j] for i in range(rb*3 , rb*3 + 3) for j in range(cb*3,cb*3+3) if board[i][j] != "."  ]


# @lc code=end

