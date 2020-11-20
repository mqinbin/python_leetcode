#
# @lc app=leetcode.cn id=771 lang=python3
#
# [771] 宝石与石头
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        js = set(J)
        answer = 0
        for char in S:
            if char in js:
                answer +=1
        return answer
# @lc code=end

