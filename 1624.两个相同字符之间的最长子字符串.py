#
# @lc app=leetcode.cn id=1624 lang=python3
#
# [1624] 两个相同字符之间的最长子字符串
#

# @lc code=start
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dic = {}
        answer = -1
        for index , char in enumerate(s):
            if char not in dic:
                dic[char] = [index , -1]
            else:
                dic[char][-1] = index
                answer = max(answer , index -dic[char][0] -1)
        return answer
# @lc code=end

