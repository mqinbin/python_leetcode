#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        return self._restoreIpAddresses(s,4)

    def _restoreIpAddresses(self, s: str,n:int):
        lens = len(s)
        if lens<n:
            return []
        if n == 1 :
            if lens <=3:
                if s.startswith('0') :
                    if  lens == 1:
                        return [s]
                    else:
                        return []
                if int(s) <256:
                    return [s]
                else:
                    return []
            else:
                return []
        answer = []
        if s.startswith('0'):
            for sub in self._restoreIpAddresses(s[1:],n-1):
                answer.append(s[0] +'.' + sub)
        else:
            if (n-1) <= lens - 1 <= (n-1) * 3:
                for sub in self._restoreIpAddresses(s[1:],n-1):
                    answer.append(s[0] + '.' + sub)
            if (n-1) <= lens - 2 <= (n-1) * 3:
                for sub in self._restoreIpAddresses(s[2:],n-1):
                    answer.append(s[:2] + '.' + sub)
            if  (n-1) <= lens - 3 <= (n-1) * 3 and  int(s[:3]) < 256:
                for sub in self._restoreIpAddresses(s[3:],n-1):
                    answer.append(s[:3] + '.' + sub)
        return answer
            


# @lc code=end

