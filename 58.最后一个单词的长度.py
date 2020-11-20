#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        try:
            last_blank_index =  s.rindex(" ")
            return len(s) -last_blank_index- 1
        except:
            return len(s)
            
        
# @lc code=end

