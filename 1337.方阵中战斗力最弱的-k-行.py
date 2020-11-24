#
# @lc app=leetcode.cn id=1337 lang=python3
#
# [1337] 方阵中战斗力最弱的 K 行
#

# @lc code=start
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def fight_pow(line :List[int]):
            answer = 0
            for p in line:
                if p == 0:
                    return answer
                answer += 1
            return answer

        helper = []
        for index, line in enumerate(mat):
            helper.append((fight_pow(line) , index))
        
        helper.sort()
        return [t[1] for t in helper ][:k]



# @lc code=end

