#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#
from typing import List
from itertools import combinations ,product
# @lc code=start
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        result = []
        for i in range(num+1):
            hours = self.dot_to_nums(i, 11)
            minutes = self.dot_to_nums(num-i, 59)
            for hv in product(hours, minutes):
                result.append("%d:%02d"%(hv[0],hv[1]))
        return result
    def dot_to_nums(self, dots,max_value, keys=[32,16,8,4,2,1]):
        
        return list(  filter(lambda v: v<=max_value  ,map(sum,combinations(keys,dots))))
      
# if __name__ == "__main__":
#     # print(Solution().dot_to_nums(2,max_value= 12))
#     print(Solution().readBinaryWatch(1))
# @lc code=end

