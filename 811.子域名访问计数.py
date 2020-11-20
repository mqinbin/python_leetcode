#
# @lc app=leetcode.cn id=811 lang=python3
#
# [811] 子域名访问计数
#

# @lc code=start
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        answer = {}

        for cpdomain in cpdomains:
            times , hosts = cpdomain.split()
            while '.' in hosts:
                answer[hosts] = answer.get(hosts,0) + int(times)
                hosts = hosts[hosts.index('.')+1:]
            answer[hosts] = answer.get(hosts,0) + int(times)
        
        return [ "%d %s" % (answer[k], k )   for k in answer]
# @lc code=end

