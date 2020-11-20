#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    dic = {0:[""],1:["()"],2:["()()","(())"]}
    def generateParenthesis(self, n: int) -> List[str]:
        if n in self.dic:
            return self.dic[n]
        
        answer = []
        for left in range(n):
            right = n- left -1
            lefts = self.generateParenthesis(left)
            rights = self.generateParenthesis(right)
            answer.extend([ "%s(%s)" % (l , r) for l in lefts for r in rights])
        return answer


        

# @lc code=end

