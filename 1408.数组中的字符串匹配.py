#
# @lc app=leetcode.cn id=1408 lang=python3
#
# [1408] 数组中的字符串匹配
#

# @lc code=start
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        all_str = " ".join(words)
        answer = []
        for word in words:
            if all_str.count(word) > 1:
                answer.append(word)
        return answer
# @lc code=end

