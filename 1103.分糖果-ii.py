#
# @lc app=leetcode.cn id=1103 lang=python3
#
# [1103] 分糖果 II
#

# @lc code=start
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        answer = [0] * num_people
        cur_candy = 1
        cur_pos = 0
        while candies > 0:
            to_give = min(candies ,cur_candy)
            answer[cur_pos] += to_give
            candies -= to_give
            cur_candy +=1
            cur_pos = (cur_pos + 1) % num_people
        return answer
            
        
# @lc code=end

