#
# @lc app=leetcode.cn id=819 lang=python3
#
# [819] 最常见的单词
#

# @lc code=start
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        from collections import Counter
        import re
        c = Counter(re.split(r'[^a-z]+' ,paragraph.lower() ))
        for kv in c.most_common():
            if kv[0]  not in banned:
                return kv[0]
        
        
# @lc code=end

