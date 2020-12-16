#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int ) -> int:
        def nTree(start,end,cache):
            if start >= end:
                return 1
            if end -start == 1:
                return 2
            
            if (end-start) in cache:
                return cache[end-start]

            answer = 0
            for i in range(start,end+1):
                left = nTree(start,i-1,cache)
                right = nTree(i+1 ,end,cache)
                answer += left * right
                # print(i, left , right)
            cache[end-start] = answer
            return answer
        return nTree(1,n,{})

# @lc code=end

