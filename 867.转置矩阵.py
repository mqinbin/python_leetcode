#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] 转置矩阵
#

# @lc code=start
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        # answer = []
        # for c in range(len(A[0])):
        #     temp = []
        #     for r in range(len(A)):
        #         temp.append(A[r][c])
        #     answer.append(temp)
        # return answer


        # return  [ for c in rane(len(A[0])) for r in range(len(A)) ]
        return zip(*A)
# @lc code=end  

