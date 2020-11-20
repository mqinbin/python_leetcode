#
# @lc app=leetcode.cn id=1078 lang=python3
#
# [1078] Bigram 分词
#

# @lc code=start
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        textl = text.split()
        answer = []
        for i in range(len(textl) - 2):
            if textl[i] == first and textl[i+1] == second:
                answer.append(textl[i+2])
        
        return answer
# @lc code=end

