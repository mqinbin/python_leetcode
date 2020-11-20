#
# @lc app=leetcode.cn id=140 lang=python3
#
# [140] 单词拆分 II
#

# @lc code=start

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # wordDict.sort(key=lambda s:len(s) )
        result = self._wordBreak(s,wordDict,{})
        return result

    def _wordBreak(self, s: str, wordDict: List[str] ,mem)-> List[str]:
        if s in mem:
            return mem[s]
        result = []
        for word in  wordDict:

            if s.startswith(word):
                if len(word) == len(s):
                    result.append(word)
                else:
                    all_last_words = self._wordBreak(s[len(word):], wordDict,mem)
                    for last_words in  all_last_words:
                        result.append( word + " " + last_words)
        mem[s] = result
        return result

# @lc code=end

