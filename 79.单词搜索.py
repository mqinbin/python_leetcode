#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0,1),(0,-1) ,(1,0),(-1,0) ]
        visted= set()
        def check(r,c,k):
            if board[r][c] != word[k]:
                return False
            if k == len(word) -1 :
                return True


            visted.add((r,c))
            result =False
            for offset in directions:
                new_r = r + offset[0]
                new_c = c + offset[1]
                if 0 <= new_r < len(board) and 0 <= new_c < len(board[0]):
                    if (new_r,new_c) not in visted and  check(new_r,new_c,k+1):
                        result = True
                        break
            # if not result:
            visted.remove((r,c))
            return result
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if check(r,c,0):
                    return True
        
        return False




# @lc code=end

