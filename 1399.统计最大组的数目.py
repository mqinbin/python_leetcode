#
# @lc app=leetcode.cn id=1399 lang=python3
#
# [1399] 统计最大组的数目
#

# @lc code=start
class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sum_place(n):
            answer = 0
            while n:
                answer += n % 10
                n //= 10
            return answer
        
        from collections import Counter

        counter = Counter( sum_place(x) for x in range(1,n+1))
        print(counter)
        times = counter.most_common(1)[0][1]
        answer = 0 
        for k,v in counter.most_common(n):
            if v == times:
                answer+=1
            else:
                break
        return answer
            


# @lc code=end

