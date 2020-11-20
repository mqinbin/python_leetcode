#
# @lc app=leetcode.cn id=942 lang=python3
#
# [942] 增减字符串匹配
#

# @lc code=start
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        l , r = 0 , len(S)
        answer = []
        for d in S:
            if d == 'I':
                answer.append(l)
                l += 1
            else:
                answer.append(r)
                r -= 1
        
        answer.append(l)
        return answer

        
# @lc code=end

