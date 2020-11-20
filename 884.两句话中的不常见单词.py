#
# @lc app=leetcode.cn id=884 lang=python3
#
# [884] 两句话中的不常见单词
#

# @lc code=start
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        from collections import Counter
        ac = Counter(A.split())
        bc = Counter(B.split())
        
        answer = []
        for k in ac.keys():
            if ac.get(k) == 1 and k not in bc:
                answer.append(k)
        
        for k in bc.keys():
            if bc.get(k) == 1 and k not in ac:
                answer.append(k)
        return answer

# @lc code=end

