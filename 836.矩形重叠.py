#
# @lc app=leetcode.cn id=836 lang=python3
#
# [836] 矩形重叠
#

# @lc code=start
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return   self.has_area(rec1) and self.has_area(rec2) and self.isLineOverlap( rec1[::2] ,rec2[::2]) and self.isLineOverlap( rec1[1::2] ,rec2[1::2])

    def has_area (self ,rec):
        if abs(rec[0]-rec[2]) * abs(rec[1]-rec[3]):
            return True
        else:
            return False

    def isLineOverlap(self,line1: List[int],line2: List[int]):
        min1 = min(line1) # 15
        min2 = min(line2) # 3
        
        max1 = max(line1) # 18
        max2 = max(line2) # 9
        #   18     3       9       3
        if max1 <= min2 or max2 <= min1:
            return False
        return True
# @lc code=end

