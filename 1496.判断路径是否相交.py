#
# @lc app=leetcode.cn id=1496 lang=python3
#
# [1496] 判断路径是否相交
#

# @lc code=start
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        cur = [0,0]
        s = set()
        s.add(tuple(cur))
        for d in path:
            if d == "N":
                cur[1] += 1 
            elif d == "E": 
                cur[0] += 1
            elif d == "W": 
                cur[0] -= 1
            elif d == "S": 
                 cur[1] -= 1 
            
            if tuple(cur) in s:
                return True
            else:
                s.add(tuple(cur))
        return False
# @lc code=end

