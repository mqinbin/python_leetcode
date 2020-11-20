#
# @lc app=leetcode.cn id=821 lang=python3
#
# [821] 字符的最短距离
#

# @lc code=start
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        desc_ans = []
        
        cur_c_index = -1
        for index , char in enumerate(S):
            if char == C:
                cur_c_index = index
                desc_ans.append(0)
            else:
                if cur_c_index == -1:
                    desc_ans.append(float('inf'))
                else:
                    desc_ans.append(index-cur_c_index)

        asc_ans = []
        cur_c_index = -1
        for index , char in enumerate(S[::-1]):
            if char == C:
                cur_c_index = index
                asc_ans.append(0)
            else:
                if cur_c_index == -1:
                    asc_ans.append(float('inf'))
                else:
                    asc_ans.append(index-cur_c_index)

        return [ min(x[0],x[1])  for x in zip (desc_ans ,asc_ans[::-1]) ]
# @lc code=end

