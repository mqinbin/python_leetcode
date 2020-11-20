#
# @lc app=leetcode.cn id=520 lang=python3
#
# [520] 检测大写字母
#

# @lc code=start
class Solution:
    ord_A = ord("A")
    ord_Z = ord("Z")
    ord_a = ord("a")
    ord_z = ord("z")

    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)

        all_same = True
        for i in range(1, len(word) -1):
            if self.is_upper(word[i]) != self.is_upper(word[i+ 1 ]):
                all_same =False
                break
        
        if all_same :
            if  self.is_upper(word[-1]) and not self.is_upper(word[0]) :
                return False
            else :
                return True
        else :
            return False
            
        
        
    def is_upper(self, char):
        return ord(char) >= self.ord_A and  ord(char) <= self.ord_Z

# @lc code=end

