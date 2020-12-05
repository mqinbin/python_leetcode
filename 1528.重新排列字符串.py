#
# @lc app=leetcode.cn id=1528 lang=python3
#
# [1528] 重新排列字符串
#

# @lc code=start
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        answer = [""] * len(s)
        for i in range(len(s)):
            answer[indices[i]] = s[i]
        return "".join(answer)
# @lc code=end

