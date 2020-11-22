#
# @lc app=leetcode.cn id=1232 lang=python3
#
# [1232] 缀点成线
#

# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def k(p1,p2):
            try:
                return (p2[1] - p1[1]) / (p2[0]  - p1[0])
            except:
                return float('inf')
        
        first_k = k(coordinates[1],coordinates[0])

        for i in range(2, len(coordinates)):
            if  k(coordinates[i],coordinates[0]) != first_k :
                return False
        return True
        

# @lc code=end

