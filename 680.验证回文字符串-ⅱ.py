#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s)-1

        change_count = 0
        while l<r:
            if s[l] == s[r]:
                l+=1
                r-=1
                continue
            else:
                change_count +=1
                
                if change_count == 2:
                    return False

                if s[l+1] == s[r]:
                    mid_s = s[l+1:r+1]
                    if mid_s == mid_s[::-1]:
                        l+=1
                        continue

                if s[r-1] == s[l]:
                    mid_s = s[l:r]
                    if mid_s == mid_s[::-1]:
                        r -=1
                        continue

                return False

                
        
        return True
        
# @lc code=end

