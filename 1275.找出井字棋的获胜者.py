#
# @lc app=leetcode.cn id=1275 lang=python3
#
# [1275] 找出井字棋的获胜者
#

# @lc code=start
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        final_state = [[None,None,None],[None,None,None],[None,None,None]]

        for i, step in enumerate(moves):
            final_state[step[0],step[1]] = i % 2
        

        def all_same_to(target, *args):
            for arg in args:
                if target != arg:
                    return False
            return True

        def is_win(state, num ):
            for 


# @lc code=end

