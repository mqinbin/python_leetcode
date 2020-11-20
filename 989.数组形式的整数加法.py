#
# @lc app=leetcode.cn id=989 lang=python3
#
# [989] 数组形式的整数加法
#

# @lc code=start
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        # answer = str(int("".join(map(str,A))) + K)
        # import re
        # return map(int,re.split(r'\B',answer))
        
        for i in range(len(A) - 1, -1 ,-1):
            K , A[i] = divmod(A[i] + K , 10)
            if K == 0:
                break
        if K:
            return list(map(int,str(K))) + A
        else:
            return A     

# @lc code=end

