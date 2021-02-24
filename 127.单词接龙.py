#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
from functools import reduce

class Solution:
    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     def diffs(word1,word2):
    #         if len(word1) == len(word2):
    #             return reduce(lambda c,t: c+(t[1]!=t[0]) , zip(word1,word2) , 0 )                
    #         else:
    #             return -1



    #     unused = set(wordList)

    #     deque = [(beginWord,0)]
        
    #     while deque:
    #         curword ,step = deque.pop(0)
    #         toDiscard = set()
    #         for word in unused:
    #             if diffs(curword, word) == 1:
    #                 if endWord == word:
    #                     return step + 2
    #                 toDiscard.add(word)
    #                 deque.append((word,step+1))
    #         unused -= toDiscard
    #         toDiscard.clear()
    #     return 0
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def diffs(word1,word2):
            if len(word1) == len(word2):
                return reduce(lambda c,t: c+(t[1]!=t[0]) , zip(word1,word2) , 0 )                
            else:
                return -1
        from collections import defaultdict
        levelDic = defaultdict(lambda :[])

        deque = [(beginWord,0)]
        
        while deque:
            curword ,step = deque.pop(0)
            toTravle = levelDic[step+1] if levelDic[step+1] else wordList
            for word in toTravle:
                diff = diffs(curword, word)
                levelDic[step+diff].append(word)
                
                if  == 1:
                    if endWord == word:
                        return step + 2
                    deque.append((word,step+1))

        return 0

# @lc code=end

