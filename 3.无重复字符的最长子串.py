#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     start = maxLength = 0
    #     usedChar = {}
        
    #     for i in range(len(s)):
    #         if s[i] in usedChar and start <= usedChar[s[i]]:
    #             start = usedChar[s[i]] + 1
    #         else:
    #             maxLength = max(maxLength, i - start + 1)

    #         usedChar[s[i]] = i

    #     return maxLength
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = dict()
        result = 0
        start_index = 0
        for index, char in enumerate(s):
            if char in char_index and  char_index[char] >= start_index:
                start_index = char_index[char] + 1
            result = max(result , index - start_index + 1 )
            char_index[char] = index
        
        return result
# @lc code=end

