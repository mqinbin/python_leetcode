#
# @lc app=leetcode.cn id=682 lang=python3
#
# [682] 棒球比赛
#

# @lc code=start
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        answers = []
        for op in ops:
            if op == "+":
                 answers.append(answers[-1] + answers[-2])
            elif op == "D":
                answers.append(answers[-1] * 2)
            elif op == "C":
                answers.pop()
            else:
                answers.append(int(op))
        
        return sum(answers)

# @lc code=end

