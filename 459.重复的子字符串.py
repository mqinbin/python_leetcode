#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        for lr in self.get_factors(len(s)):
            if s[lr:] + s[:lr] == s:
                return True
        return False

    def get_factors (self, n):
        result = []
        for f in range(1,int(n**0.5)+1):
            if n% f == 0:
                if n != f:
                    result.append(f)
                if f != n//f and f != 1:
                    result.append(n//f)
        return result

if __name__ == "__main__":
    print(Solution().get_factors(4))
# @lc code=end

