#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        answer = 0
        repeats = [1]
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                repeats[-1] += 1
            else:
                repeats.append(1)
        
        print(repeats)
        for i in range(1, len(repeats)):
            answer += min(repeats[i],repeats[i-1])
        return answer

# @lc code=end

