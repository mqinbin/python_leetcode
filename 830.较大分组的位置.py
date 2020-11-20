#
# @lc app=leetcode.cn id=830 lang=python3
#
# [830] 较大分组的位置
#

# @lc code=start
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        
        last_char = None
        last_start = 0
        result = []
        for i, char in enumerate(s):
            if char != last_char:
                if i - last_start >= 3:
                    result.append([last_start , i-1])
                last_start = i
                last_char = char
        i+=1
        if i - last_start >= 3:
            result.append([last_start , i-1])
        return result
# @lc code=end

