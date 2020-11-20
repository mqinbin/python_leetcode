#
# @lc app=leetcode.cn id=748 lang=python3
#
# [748] 最短补全词
#

# @lc code=start

import re
from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = re.sub(r'[^a-z]',"" ,licensePlate.lower())
        lc = Counter(licensePlate)
        dic = {}
        for word in sorted(words,key=lambda w: (len(w))):
            if not lc - Counter(word) :
                return word
        return ""

# @lc code=end

