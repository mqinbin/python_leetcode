#
# @lc app=leetcode.cn id=223 lang=python3
#
# [223] 矩形面积
#

# @lc code=start
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        def incert(lineA,lineB):
            return max(0 ,  min(max(lineA) ,max(lineB) ) - max(min(lineA) , min(lineB)))

        incertArea =  incert((A,C),(E,G)) * incert((B,D),(F,H))
        first = abs(A-C) * abs(B-D)
        second = abs(E-G) * abs(F-H)
        return first + second - incertArea



# @lc code=end

