#
# @lc app=leetcode.cn id=492 lang=python3
#
# [492] 构造矩形
#

# @lc code=start
from typing import List
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        fs = self.factors(area)
        mid = len(fs)//2 - 1
        return fs[mid:mid+2]


    def factors(self,n):
        result = []
        for f in range(1, int(n ** 0.5 )+1):
            if n % f == 0:
                result.append(f)
                result.append(n//f)
        result.sort(reverse=True)
        return result
    

    
# @lc code=end

