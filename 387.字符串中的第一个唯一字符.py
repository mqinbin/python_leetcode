#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        first_dict  = dict()
        more_set = set()

        for index, char in enumerate(s):
            if char in first_dict:
                del first_dict[char]
                more_set.add(char)
            else:
                if char in more_set:
                    continue
                else:
                    first_dict[char] = index
        print(first_dict)
        if first_dict:
            return sorted(first_dict.values())[0]
        else:
            return -1


# @lc code=end

