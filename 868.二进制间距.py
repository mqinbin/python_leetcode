#
# @lc app=leetcode.cn id=868 lang=python3
#
# [868] 二进制间距
#

# @lc code=start
class Solution:
    def binaryGap(self, n: int) -> int:
        
        index = 0
        last_one_index = 0
        answer = 0
        while n > 0:
            index +=1

            if n & 1:
                if last_one_index:
                    answer = max(index - last_one_index,answer)
                last_one_index = index

            n >>=1
        return answer
# @lc code=end

