#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # from collections import Counter
        # sc = Counter(s)
        # tc = Counter(t)
        # return list((tc-sc).keys())[0]
        return chr(sum(map(ord,t)) - sum(map(ord,s)))
if __name__ == "__main__":
    Solution().findTheDifference("abcd" , "abcde")
# @lc code=end

