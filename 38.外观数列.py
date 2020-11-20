#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
def xx(m:re.Match):
    return str(len(m.group(0))) + m.group(1)

class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n-1):
            s = re.sub(r"(\d)\1*" , xx , s)
        return s
# @lc code=end

