#
# @lc app=leetcode.cn id=1380 lang=python3
#
# [1380] 矩阵中的幸运数
#

# @lc code=start
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_in_rows = list(map(min,matrix))
        max_in_cols = list(map(max,zip(*matrix)))
        # print(min_in_rows)
        # print("----------")
        # print(max_in_cols)
        answer = []
        for num in min_in_rows:
            if num in max_in_cols:
                answer.append(num)
        return answer


    
# @lc code=end

