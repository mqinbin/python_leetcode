#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split()
        if len(pattern)!= len(words):
            return False
        helper1 = {}
        helper2 = {}
        for i,word in enumerate(words):
            if pattern[i] in helper1 and helper1[pattern[i]] !=word:
                return False
            if  word in helper2 and helper2[word] !=pattern[i]:
                return False
            helper1[pattern[i]] = word
            helper2[word] = pattern[i]
        return True
        

# @lc code=end

