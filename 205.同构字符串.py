#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        st ={}
        ts = {}
        for i in range(n):
            if s[i] in st and t[i] in ts:
                if st[s[i]] == t[i] and ts[t[i]] == s[i]:
                    pass
                else:
                    return False
            elif s[i] not in st and t[i] not in ts:
                st[s[i]] = t[i]
                ts[t[i]] = s[i]
            else:
                return False
        return True
# @lc code=end

