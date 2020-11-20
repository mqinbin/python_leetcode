#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_len = len(strs[0])
        for s in strs:
            min_len = len(s) if len(s) < min_len else min_len
        
        result = 0
        for index in range(min_len):
            char = strs[0][index]
            match = True
            for s in strs:
                if s[index] != char:
                    match = False
                    break
            if match:
                result +=1
            else:
                break        
        return strs[0][:result]
        

# @lc code=end

