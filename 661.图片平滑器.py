#
# @lc app=leetcode.cn id=661 lang=python3
#
# [661] 图片平滑器
#

# @lc code=start
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        rn = len(M)
        cn = len(M[0])
        
        result = []


        for r in range(rn):
            temp = []
            top = max(0, r-1)
            bottom = min(r+1,rn-1) + 1
            
            for c in range(cn):
                left = max(0 , c-1)
                right = min(c+1, cn-1) +1
                total = 0
                for i in range(top, bottom):
                    total += sum(M[i][left:right])
                temp.append(total // ((bottom-top) * (right - left)) )

            result.append(temp)
        return result
# @lc code=end

