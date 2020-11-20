#
# @lc app=leetcode.cn id=1037 lang=python3
#
# [1037] 有效的回旋镖
#

# @lc code=start
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        if points[0] == points[1] or points[1] == points[2]  or points[2] == points[0]:
            return False 

        def k(p1,p2):
            try:
                return  (p1[1] - p2[1])/ (p1[0] - p2[0])
            except ZeroDivisionError:
                return float('inf')

        k1 = k(points[1], points[0])    
        k2 = k(points[2], points[0]) 
        return k1 != k2
# @lc code=end

