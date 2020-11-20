#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        si = len(S)-1
        ti = len(T)-1
        while True:
            si = self.find_compare_pos(S,si)
            ti = self.find_compare_pos(T,ti)
            # print(si,ti)
            if si == -1 and ti ==-1:
                return True
            if si == -1 or ti ==-1:
                return False
            if S[si] == T[ti]:
                si -=1
                ti -=1
            else:
                return False
            
        
        
    def find_compare_pos(self, string, index):
        if index == -1 or string[index] != "#":
            return index
        
        # ab#c
        # index  4
        # skip 0
        skip = 0
        while index >= 0:
            if string[index] == "#":
                skip += 1
                index -= 1
            elif skip:
                skip -= 1
                index -= 1
            else:
                return index
        return index

        
# @lc code=end

