#
# @lc app=leetcode.cn id=1175 lang=python3
#
# [1175] 质数排列
#

# @lc code=start
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def A(up,down):
            answer = 1
            for _ in range(up):
                answer *= down
                down -= 1
            return answer
        
        def count_primary(n):
            answer = [1] * (n + 1)
            answer[0:3] = [0,0,1]
            for i in range(2, n + 1):
                if answer[i] == 0:
                    continue
                j = i + i
                while j < n + 1:
                    answer[j] = 0
                    j+=i
            return answer.count(1)
        
        primarys = count_primary(n)
        return A(primarys ,primarys) * A ( n - primarys , n - primarys) % ( 10**9 + 7 )


# @lc code=end

