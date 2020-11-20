#
# @lc app=leetcode.cn id=985 lang=python3
#
# [985] 查询后的偶数和
#

# @lc code=start
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = sum([x for x in A if x % 2 == 0])
        result = []
        for query in queries:
            v ,index = query
            if A[index] % 2 == 0:
                evenSum -= A[index]
            
            A[index] +=v
            if A[index] % 2 == 0:
                evenSum += A[index]
            result.append(evenSum)
        return result


        
# @lc code=end

