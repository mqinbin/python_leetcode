#
# @lc app=leetcode.cn id=1598 lang=python3
#
# [1598] 文件夹操作日志搜集器
#

# @lc code=start
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cur_depth = 0
        for op in logs:
            if op.startswith(".."):
                cur_depth = max(cur_depth-1,0)
            elif op.startswith("."):
                pass
            else:
                cur_depth += 1
        return cur_depth
# @lc code=end

