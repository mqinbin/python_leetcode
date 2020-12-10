#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for index , word in enumerate(strs):
            sword = "".join(sorted(word))
            if sword not in dic:
                dic[sword] = []
            dic[sword].append(index)
        
        return [[strs[i] for i in v] for v in dic.values()]

# @lc code=end

