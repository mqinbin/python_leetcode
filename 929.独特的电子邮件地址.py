#
# @lc app=leetcode.cn id=929 lang=python3
#
# [929] 独特的电子邮件地址
#

# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        import re
        answer = set()
        for email in emails:
            name , host = email.split("@")
            answer.add(  ( re.sub(r'\.|\+.*','' , name),host) )

        return len(answer)
# @lc code=end

