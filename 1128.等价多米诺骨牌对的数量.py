#
# @lc app=leetcode.cn id=1128 lang=python3
#
# [1128] 等价多米诺骨牌对的数量
#

# @lc code=start
class Solution:
    # def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
    #     dic = {}
    #     for dominoe in dominoes:
    #         _sum = dominoe[0] + dominoe[1]
    #         if _sum not in dic:
    #             dic[_sum] = []
    #         dic[_sum].append([min(dominoe) ,max(dominoe)])
        
    #     print(dic)
    #     answer = 0

    #     for sets in dic.values():
    #         if len(sets) < 2:
    #             continue
    #         sets.sort()
    #         sets.append([0,0])
    #         f = -1
    #         same_nums = 0
    #         for dominoe in sets:
    #             if dominoe[0] == f:
    #                 same_nums += 1
    #             else:
    #                 answer += same_nums * (same_nums -1) // 2
    #                 f = dominoe[0]
    #                 same_nums = 1
    #     return answer
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dic = {}
        for dominoe in dominoes:
            t = tuple( dominoe if dominoe[0] <= dominoe[1] else dominoe[::-1]  )
            dic[t] = dic.get(t ,0 ) + 1
        
        answer = 0
        for v in dic.values():
            answer += v * (v-1) // 2
        return answer
# @lc code=end

