#
# @lc app=leetcode.cn id=937 lang=python3
#
# [937] 重新排列日志文件
#

# @lc code=start
class Solution:
    def key(self,log):
        tag, content = log.split(" " , 1)
        if ord('a') <= ord(content[0]) <=ord('z'):
            return (0, content,tag)
        else:
            return (1,0)
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs, key=self.key)
# @lc code=end

