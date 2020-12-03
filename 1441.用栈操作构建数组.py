#
# @lc app=leetcode.cn id=1441 lang=python3
#
# [1441] 用栈操作构建数组
#

# @lc code=start
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        last_num = target[-1]
        target_index = 0
        target_len = len(target)
        answer = []
        # for num in range(1,n+1):
        num = 1
        while True:
            if num > last_num:
                break
            if num == target[target_index]:
                target_index += 1
                answer.append("Push")
            else:
                answer.append("Push")
                answer.append("Pop")
            num += 1
        return answer
# @lc code=end

