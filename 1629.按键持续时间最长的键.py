#
# @lc app=leetcode.cn id=1629 lang=python3
#
# [1629] 按键持续时间最长的键
#

# @lc code=start
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        answer = keysPressed[0]
        cur_max = 0
        start = 0
        for index, time in enumerate(releaseTimes):
            value  =  (time - start)
            start = time
            if value > cur_max  or (value == cur_max and ord(keysPressed[index]) > ord(answer)):
                answer =  keysPressed[index]
                cur_max =  value
                
        return answer

# @lc code=end

