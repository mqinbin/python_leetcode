#
# @lc app=leetcode.cn id=1356 lang=python3
#
# [1356] 根据数字二进制下 1 的数目排序
#

# @lc code=start
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_one(n):
            answer = 0
            while n:
                n = n & (n-1)
                answer += 1
            return answer
        
        return sorted(arr, key = lambda n: ( count_one(n),n ) )
# @lc code=end

