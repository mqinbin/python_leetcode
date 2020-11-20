#
# @lc app=leetcode.cn id=299 lang=python3
#
# [299] 猜数字游戏
#

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = 0
        for i in range(len(secret)):
            if guess[i] == secret[i]:
                a+=1
        from collections import Counter

        b = len( secret) - sum( (Counter(secret) - Counter(guess)).values()) - a
        return '%dA%dB' % (a,b)

# @lc code=end

