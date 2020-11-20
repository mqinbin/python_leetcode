#
# @lc app=leetcode.cn id=997 lang=python3
#
# [997] 找到小镇的法官
#

# @lc code=start
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        fg = set()
        for i in range(N):
            fg.add(i+1)
        for t in trust:
            if t[0] in fg:
                fg.remove(t[0])
        if len(fg)!=1:
            return -1
        
        fg_id = fg.pop()
        del fg

        qz = set()
        for t in trust:
            if t[1] == fg_id:
                qz.add(t[0])
        
        if len(qz) !=  N-1:
            return -1
        return fg_id

# @lc code=end

