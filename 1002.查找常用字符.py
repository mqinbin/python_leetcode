#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找常用字符
#

# @lc code=start
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        from collections import Counter
        answer = Counter(A[0])
        for word in A:
            answer &= Counter(word)
        result = []
        for k, v in answer.items():
            result += [k] * v
        return result

# @lc code=end

