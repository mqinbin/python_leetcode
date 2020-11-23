#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []



        def dfs(begin, candidates, residue, path, res):
            if residue == 0:
                res.append(path[:])
                return

            for i in range(begin, len(candidates)):
                if candidates[i] > residue:
                    print("    " , "break",i,candidates[i] )
                    break
                if i > begin and candidates[i] == candidates[i - 1]:
                    print("    " , "continue",i,candidates[i] )
                    continue

                path.append(candidates[i])
                dfs(i + 1, candidates, residue - candidates[i], path, res)
                path.pop()


        candidates.sort()
        size = len(candidates)
        res = []
        dfs(0, candidates, target, [], res)
        return res
# @lc code=end

