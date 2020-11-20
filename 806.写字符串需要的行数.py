#
# @lc app=leetcode.cn id=806 lang=python3
#
# [806] 写字符串需要的行数
#

# @lc code=start
class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        

        lines = 1
        offset = 0
        for char in S:
            cost = widths[ord(char) - ord('a')]
            if offset + cost >100:
                lines += 1
                offset = cost
            else:
                offset +=cost
        
        return [lines, offset]

        
# @lc code=end

