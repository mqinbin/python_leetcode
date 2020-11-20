#
# @lc app=leetcode.cn id=944 lang=python3
#
# [944] 删列造序
#

# @lc code=start
class Solution:

    def non_desc(self,iter):
        last = ord('a') - 1
        for char in iter:
            if ord(char) < last:
                return False
            last = ord(char)
        return True

    def minDeletionSize(self, A: List[str]) -> int:
        answer = 0
        for x in zip(*A):
            answer += 1 - self.non_desc(x)
        return answer
# @lc code=end

