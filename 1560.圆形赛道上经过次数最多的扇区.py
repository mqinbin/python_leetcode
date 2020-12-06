#
# @lc app=leetcode.cn id=1560 lang=python3
#
# [1560] 圆形赛道上经过次数最多的扇区
#

# @lc code=start
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:

        # def offset(sec, n):
        #     return ((sec - 1) % n ) + 1
        # cur = rounds[0]
        # answer = [cur]
        # for i in range(1, len(rounds)):
        #     while True:
        #         cur = offset(cur + 1, n)
        #         answer.append(cur)
        #         if cur == rounds[i]:
        #             break
        # from collections import Counter
        # counter = Counter(answer)
        # return sorted([k for k,v in counter.items() if v == counter.get(rounds[0])])
        
        first = rounds[0]
        last = rounds[-1]
        if last >= first:
            return [x for x in range(first, last + 1)]
        else:
            return sorted( list(set(range(1,n+1) ) -  set(range(last+1,first)) ) )
            




# @lc code=end

