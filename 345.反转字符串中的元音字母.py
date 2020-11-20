#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        # vowels = ("a","e","i","o","u","A","E","I","O","U")
        # n = len(s)
        # left = 0
        # right = n-1
        # sl = list(s)
        # while left < right:
        #     while left < right and s[left] not in vowels:
        #         left+=1
        #     while  left < right and  s[right] not in vowels:
        #         right-=1
        #     sl[left],sl[right] =  sl[right],sl[left] 
        #     left +=1
        #     right -=1

        # return "".join(sl)
        import re
        vowels = re.findall(r'(?i)[aeiou]',s)
        return re.sub(r'(?i)[aeiou]' , lambda m: vowels.pop(),s) 
# @lc code=end

