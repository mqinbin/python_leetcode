#
# @lc app=leetcode.cn id=953 lang=python3
#
# [953] 验证外星语词典
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = { v:i for i,v in enumerate(order)}
        def key(word):
            return  tuple (map(lambda c: dic[c] , word) )
        return words == sorted(words, key=key)
# @lc code=end

