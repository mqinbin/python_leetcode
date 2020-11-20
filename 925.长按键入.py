#
# @lc app=leetcode.cn id=925 lang=python3
#
# [925] 长按键入
#

# @lc code=start
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        ni = 0 
        for ti in range(len(typed)):
            if ni < len(name) and name[ni] == typed[ti]:
                ni += 1
            elif  ni > 0 and name[ni-1] == typed[ti]:
                continue
            else:
                return False
        return ni == len(name)
# @lc code=end

