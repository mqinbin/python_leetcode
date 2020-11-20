#
# @lc app=leetcode.cn id=1071 lang=python3
#
# [1071] 字符串的最大公因子
#

# @lc code=start
import math
class Solution:
    # def gcdOfStrings(self, str1: str, str2: str) -> str:
    #     max_result = math.gcd(len(str1), len(str2))

    #     def is_repeate(full: str, pattern: str):
    #         pn = len(pattern)
    #         for i in range(0, len(full), pn):
    #             if full[i:i+pn] != pattern:
    #                 return False
    #         return True

    #     def factors(n: int) -> List[int]:
    #         return [i for i in range(n,0,-1) if n % i == 0]

    #     for f in factors(max_result):
    #         if is_repeate(str1,str1[0:f]) and is_repeate(str2,str1[0:f]):
    #             return str1[0:f]
    #     return ""

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if ( str1 + str2 ) != ( str2 + str1 ):
            return ''
			
        elif str1 == str2:
            return str1
			
        else:
            length_by_gcd = math.gcd( len(str1), len(str2) )
            return self.gcdOfStrings( str1[:length_by_gcd], str2[:length_by_gcd] )


# @lc code=end

