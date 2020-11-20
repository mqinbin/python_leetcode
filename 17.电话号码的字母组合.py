#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    dic = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        if digits:
            if len(digits) == 1:
                return [x for x in self.dic[digits[0]]]
            else:
                for char in self.dic[digits[0]]:
                    for last in self.letterCombinations(digits[1:]):
                        answer.append(char+last)
        return answer
# @lc code=end

