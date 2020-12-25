#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = tuple(map(int,version1.split('.')))
        v2 = tuple(map(int,version2.split('.')))
        max_len = max(len(v1),len(v2))
        dummy = [0] * max_len

        for i in range(max_len):
            s1  = v1[i] if i < len(v1) else dummy[i]
            s2  = v2[i] if i < len(v2) else dummy[i]
            if s1<s2:
                return -1
            if s1>s2:
                return 1
        
        return 0

# @lc code=end

