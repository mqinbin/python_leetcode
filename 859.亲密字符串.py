#
# @lc app=leetcode.cn id=859 lang=python3
#
# [859] 亲密字符串
#

# @lc code=start
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        a_diffIndex = []
        for i in range(len(A)) :
            if A[i] != B[i]:
                a_diffIndex.append(i)
        diffs = len(a_diffIndex)
        if diffs>2 or diffs ==1:
            return False
        if diffs == 0:
            return len(set(A)) != len(A)
        return A[a_diffIndex[0]] == B[a_diffIndex[1]] and A[a_diffIndex[1]] ==B[a_diffIndex[0]]




# @lc code=end

