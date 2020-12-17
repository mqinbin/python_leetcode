#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        return self._numDecodings(s,dict())

    def _numDecodings(self, s: str,cache:dict) -> int:
        if s in cache:
            return cache[s]
        answer = 0
        if s.startswith('0'):
            return 0

        lens = len(s)
        if lens == 1:
            return 1
        if lens == 2:
            if s[1] == '0' :
                return self.validate(s) - 0
            else:
                return self.validate(s) + 1
        
        answer += self._numDecodings(s[1:],cache)
        if self.validate(s[:2]):
            answer += self._numDecodings(s[2:],cache)

        cache[s] = answer
        return answer
    


    def validate(self, s:str):
        return  int(s) <= 26



# @lc code=end

