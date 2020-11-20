#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index in range(len(numbers) ):
            find = self.find_index(numbers,index+1,len(numbers) ,target -numbers[index] ) 
            if find > 0:
                return [index + 1 , find + 1]
        
        return []

    def find_index(self, numbers, start, end, target):
        while start < end :
            mid  = (start + end) // 2
            if target == numbers[mid]:
                return mid
            if  numbers[mid] > target :
                end  = mid
            else:
                start = mid + 1
        return -1
# @lc code=end

