#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        
        index_A = ord("A")
        result = ""
        while True:
            n-=1
            result =  chr( (n  % 26)  + index_A ) +result
            n //=26
            if n == 0:
                break
        return result
# @lc code=end

