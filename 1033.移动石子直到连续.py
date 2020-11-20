#
# @lc app=leetcode.cn id=1033 lang=python3
#
# [1033] 移动石子直到连续
#

# @lc code=start
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        helper = [a,b,c]
        helper.sort()
        if helper[1]- helper[0] == 1 and helper[2]- helper[1] == 1:
            return [0,0]
        
        if helper[1]- helper[0] == 1 or helper[2]- helper[1] == 1:
            return [1,helper[2] - helper[0] - 2]
        
        
# @lc code=end

