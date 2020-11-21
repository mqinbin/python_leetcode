#
# @lc app=leetcode.cn id=1170 lang=python3
#
# [1170] 比较字符串最小字母出现频次
#

# @lc code=start
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(word):
            word = list(word)
            word.sort()
            return word.count(word[0])
        
        query = [f(x) for x in queries]
        word = [f(x) for x in words]

        answer = []
        for x in query:
            # count = 0
            # for y in word:
            #     if x < y:
            #         count += 1
            # answer.append(count)
            answer.append( sum( [x<y for y in word]) )
        return answer
# @lc code=end

