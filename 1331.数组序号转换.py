#
# @lc app=leetcode.cn id=1331 lang=python3
#
# [1331] 数组序号转换
#

# @lc code=start
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        helper = sorted(arr)
        dic = {}

        order = 0
        cur = float('-inf')
        for n in helper:
            if n != cur:
                order += 1
                dic[n] = order
                cur = n


        return [dic[x]  for x in arr]        


# @lc code=end

