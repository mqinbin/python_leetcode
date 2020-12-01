#
# @lc app=leetcode.cn id=820 lang=python3
#
# [820] 单词的压缩编码
#

# @lc code=start
class Solution:
    # def minimumLengthEncoding(self, words: List[str]) -> int:
    #     words = set(words)
    #     trie = {}
    #     leaf_nodes = []
    #     for word in words:
    #         now = trie
    #         for char in word[::-1]:
    #             if char not in now:
    #                 now[char] = {}
    #             now = now[char]
    #         leaf_nodes.append(now)
        
        
    #     answer = 0
    #     for word,node in zip(words,leaf_nodes):        
    #         if not node:
    #             answer += len(word) + 1
    #     return answer
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = set(words)
        from collections import defaultdict
        from functools import reduce
        Trie = lambda : defaultdict(Trie)
        trie = Trie()
        leaf_nodes = [ reduce(dict.__getitem__,word[::-1] , trie) for word in words]
        answer = sum([ len(word) + 1 for word ,node in zip(words,leaf_nodes) if not node ])
        return answer
# @lc code=end

