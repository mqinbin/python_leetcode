#
# @lc app=leetcode.cn id=888 lang=python3
#
# [888] 公平的糖果交换
#

# @lc code=start
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        a_sum = sum(A) 
        b_sum = sum(B) 
        total = a_sum + b_sum
        target = total // 2
        a_set = set(A)
        b_set = set(B)
        
        answer = []
        for candy in a_set:
            if b_sum + candy - target in b_set: 
                return [candy,  b_sum + candy - target]
# @lc code=end

