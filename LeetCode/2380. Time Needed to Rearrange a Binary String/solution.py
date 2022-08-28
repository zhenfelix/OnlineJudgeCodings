class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        res, cnt = 0, 0
        for c in s:
            if c == '0': cnt += 1
            elif cnt: res = max(res + 1, cnt)
        return res


# 作者：newhar
# 链接：https://leetcode.cn/problems/time-needed-to-rearrange-a-binary-string/solution/by-newhar-o6a1/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        ans, cnt, pre = 0, 0, 0
        for ch in s:
            if ch == '1':
                if cnt > 0:
                    cur = max(cnt, pre+1)
                    ans = max(ans, cur)
                    pre = cur 
            else:
                cnt += 1
        return ans

class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        res = 0
        while True:
            t = s.replace("01", "10")
            if s == t:
                break
            res += 1
            s = t
        return res


class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        cnt = 0
        s = list(s)
        n = len(s)
        flag = True 
        while flag:
            flag = False
            cur = 0
            while cur < n:
                if cur+1 < n and s[cur] == '0' and s[cur+1] == '1':
                    s[cur], s[cur+1] = '1', '0'
                    cur += 2
                    flag = True 
                else:
                    cur += 1
            if flag:
                cnt += 1
        return cnt