#
# @lc app=leetcode.cn id=720 lang=python3
#
# [720] 词典中最长的单词
#

# @lc code=start
class Solution:
    def longestWord(self, words: List[str]) -> str:
        dic = {}
        for word in words:
            l = len(word)
            if l in dic:
                dic[l].append(word)
            else:
                dic[l] = [word]
        for k in dic:
            dic[k].sort()
        
        for l in sorted(dic.keys(),reverse=True):
            for word in dic[l]:
                if self._wordMatch(word,dic):
                    return word
        return ""        
    
    def _wordMatch(self, word, dic):
        l = len(word)
        if l == 1:
            return True 
        if l-1 not in dic:
            return False
        for w in dic[l-1]:
            if w == word[:-1]:
                return self._wordMatch(w,dic)
        return False



        
# @lc code=end

