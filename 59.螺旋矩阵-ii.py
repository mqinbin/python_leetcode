#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        A, lo = [], n*n+1
        while lo > 1:
            lo, hi = lo - len(A) , lo
            A = list(zip(*A[::-1]))
            A.insert(0,list(range(lo,hi)))
            print(A)
        return A
# @lc code=end

