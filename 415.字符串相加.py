#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
from itertools import zip_longest
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        zip = zip_longest(num1[::-1],num2[::-1],fillvalue='0')

        result = 0
        offset = 0
        for x in zip:
            cv = ord(x[0]) + ord(x[1]) - 2 *ord('0')
            result = result  + cv * 10 **offset
            offset+=1
            # print(x[0], x[1] , cv, result)
        
        return str(result)
        # return str(
        #       reduce(lambda a, b: 10*a + b, 
        #          map(lambda x: ord(x[0])+ord(x[1])-2*ord('0'),
        #            list(zip_longest(num1[::-1], num2[::-1], fillvalue='0'))[::-1]
        #          ) 
        #       )
        #     )
# @lc code=end

