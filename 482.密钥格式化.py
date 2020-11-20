#
# @lc app=leetcode.cn id=482 lang=python3
#
# [482] 密钥格式化
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.upper().replace("-","")
        mod = len(S)% K
        result = ""
        if mod:
            result += S[:mod]+"-"
        for x in range(mod,len(S),K):
            result += S[x:x+K] +"-"
        result = result[:-1]
        return result
# @lc code=end

