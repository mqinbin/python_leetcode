#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        answer = []
        temp = []
        n = len(nums)
        cur_min = float('inf')
        from bisect import bisect
        for f in range(n-2):
            if f > 0 and nums[f] == nums[f - 1]:
                continue
            temp.append(nums[f])
            for s in range(f+1,n-1):
                if s > f+1 and nums[s] == nums[s - 1]:
                    continue
                two_sum =  nums[s] + nums[f]
                temp.append(nums[s])
                ti = bisect(nums, target - two_sum)
                if ti-1 > s:
                    diff  = abs(two_sum+ nums[ti-1] - target)
                    if diff < cur_min:
                        cur_min = diff
                        answer = [nums[f] , nums[s] , nums[ti-1]]
                if ti > s:
                    ti = min(ti, n-1)
                else:
                    ti = max(ti,s+1)

                diff  = abs(two_sum + nums[ti] - target)
                if diff < cur_min:
                    cur_min = diff
                    answer = [nums[f] , nums[s] , nums[ti] ]
                temp.pop()
            temp.pop()
        print(answer)
        return sum(answer)
        
# @lc code=end

