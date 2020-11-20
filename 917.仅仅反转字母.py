#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        left = 0 
        S  = [x for x in S]
        right = len(S) - 1

        while left < right:
            while left<right and not S[left].isalpha():
                left += 1
            while left<right and not S[right].isalpha():
                right -= 1
            S[left] ,S[right] =S[right] , S[left] 
            left += 1
            right -= 1
        return "".join(S)

    

# @lc code=end

