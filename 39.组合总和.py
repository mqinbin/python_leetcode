#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 1 :
            if target < candidates[0]:
                return []
            elif target % candidates[0] == 0:
                return [candidates * (target // candidates[0])]
            else:
                return []

        candidates.sort(reverse=True)

        result = []
        for i in range(target // candidates[0] + 1):
            last =target - i * candidates[0]
            if last > 0:
                soluves = self.combinationSum(candidates[1:] , last)
                if soluves:
                    for s in soluves:
                        result.append([candidates[0]] * i + s )
            elif last == 0:
                result.append([candidates[0]] * i )
        return result

# @lc code=end
