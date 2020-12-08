#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    # 马拉车 没懂
    # def longestPalindrome(self, s: str) -> str:

    # 中心扩散
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        n = len(s)
        answer = s[0]
        for center in range(0, n):
            odd_expand = self.expand(s,center, center)
            even_expand = self.expand(s,center, center+1)
            if len(odd_expand) > len(answer):
                answer = odd_expand
            if len(even_expand) > len(answer):
                answer = even_expand
                    
        return answer
            

    def expand(self,s,left,right):
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return s[left+1:right]



    # 动态规划
    # def longestPalindrome(self, s: str) -> str:
    #     if len(s) < 2:
    #         return s
    #     n = len(s)
    #     dp = [ [None] * n for _ in range(n)  ]
    #     for i in range(n):
    #         dp[i][i] = True

    #     answer = [0,0] # start, end  include
    #     for col in range(1,n):
    #         for row in range(col):
    #             dp[row][col] = (s[row] == s[col]) and (col-row==1 or dp[row+1][col-1])
    #             if dp[row][col] and col-row > answer[1]-answer[0]:
    #                 answer = [row,col]
    #     return s[answer[0] :answer[1] + 1]


    # 暴力解法，超时
    # def longestPalindrome(self, s: str) -> str:
    #     if len(s) < 2:
    #         return s
    #     answer = [0,1] # start len
    #     for left in range(0,len(s)-1):
    #         for right in range(len(s)-1, left,-1):
    #             if self.isPalindrome(s,left,right):
    #                 print(s[left:right+1])
    #                 if right-left +1 > answer[1]:
    #                     answer = [left, right-left +1]
        
    #     return s[answer[0]:answer[0]+answer[1]]
    
    def isPalindrome(self, s, start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
# @lc code=end

