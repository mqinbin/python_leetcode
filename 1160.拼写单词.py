#
# @lc app=leetcode.cn id=1160 lang=python3
#
# [1160] 拼写单词
#

# @lc code=start
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import Counter
        chars_counter = Counter(chars)
        # answer = 0
        # for word in words:
        #     if not Counter(word) - chars_counter:
        #         answer += len(word)
        
        # return answer
        return sum([len(word) for word in words if not Counter(word) - chars_counter])

# @lc code=end

