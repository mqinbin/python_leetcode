#
# @lc app=leetcode.cn id=1030 lang=python3
#
# [1030] 距离顺序排列矩阵单元格
#

# @lc code=start
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        
        def mhd(rc):
            return ( abs(rc[0] -r0) + abs(rc[1] - c0) )

        return sorted( [(i,j) for i in range(R) for j in range(C)] ,key = mhd)

# @lc code=end

