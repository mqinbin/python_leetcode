#
# @lc app=leetcode.cn id=1304 lang=python3
#
# [1304] 和为零的N个唯一整数
#

# @lc code=start
class Solution:
    def sumZero(self, n: int) -> List[int]:
        answer = []
        for i in range(- (n // 2) , 0):
            answer.append(i)
        if n&1:
            answer.append(0)
        for i in range( 1, n// 2 +1):
            answer.append(i)
        return answer
        
# @lc code=end

