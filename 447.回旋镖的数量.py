#
# @lc app=leetcode.cn id=447 lang=python3
#
# [447] 回旋镖的数量
#

# @lc code=start
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        result = 0
        for pi in points:
            d_pi_count = {}
            for pj in points:
                if pi is pj : continue
                distance = (pi[0] - pj[0]) ** 2 + (pi[1] - pj[1]) ** 2 
                d_pi_count[distance] = d_pi_count.get(distance,0) + 1
            
            for v in d_pi_count.values():
                result += v * (v-1)


        return result

# @lc code=end

