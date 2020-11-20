#
# @lc app=leetcode.cn id=999 lang=python3
#
# [999] 可以被一步捕获的棋子数
#

# @lc code=start
class Solution:
    # def numRookCaptures(self, board: List[List[str]]) -> int:
    #     dic = {}
    #     for r in range(len(board)):
    #         for c in range(len(board[r])):
    #             char = board[r][c]
    #             if char != '.':
    #                 if char not in dic:
    #                     dic[char] = set()
    #                 dic[char].add((r,c))
        
    #     r_pos = dic['R'].pop()
    #     answer = 0
    #     for x in range(r_pos[0] + 1, len(board)):
    #         if 'B' in dic and  (x,r_pos[1]) in dic['B']:
    #             break
    #         if 'p' in dic and (x,r_pos[1]) in dic['p']:
    #             answer+=1
    #             break
    #     for x in range(r_pos[0] - 1, -1,-1):
    #         if 'B' in dic and  (x,r_pos[1]) in dic['B']:
    #             break
    #         if 'p' in dic and (x,r_pos[1]) in dic['p']:
    #             answer+=1
    #             break    
    #     for y in range(r_pos[1] + 1, len(board[r_pos[0]])):
    #         if 'B' in dic and  (r_pos[0],y) in dic['B']:
    #             break
    #         if 'p' in dic and (r_pos[0],y) in dic['p']:
    #             answer+=1
    #             break   
    #     for y in range(r_pos[1] - 1, -1,-1):
    #         if 'B' in dic and  (r_pos[0],y) in dic['B']:
    #             break
    #         if 'p' in dic and (r_pos[0],y) in dic['p']:
    #             answer+=1
    #             break
    #     return answer

        def numRookCaptures(self, B: List[List[str]]) -> int:
            y, x = next((i, j) for j in range(8) for i in range(8) if B[i][j] == 'R')
            print(y,x)
            row = ''.join(B[y][j] for j in range(8) if B[y][j] != '.')
            col = ''.join(B[i][x] for i in range(8) if B[i][x] != '.')
            print(row)
            print(col)
            return sum('Rp' in s for s in (row, col)) + sum('pR' in s for s in (row, col))
# @lc code=end

