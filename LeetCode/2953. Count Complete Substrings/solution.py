# https://leetcode.cn/problems/count-complete-substrings/solutions/2551713/xiao-yang-xiao-en-o26n-xian-kao-lu-hou-y-gpbr/
class Solution:
    def countCompleteSubstrings(self, w: str, k: int) -> int:
        def calc(s):
            res = 0
            v = len(s)
            for i in range(1, 27):
                if i * k > v: break
                l = i * k
                cnt = Counter(s[:l])
                freq = Counter(cnt.values())
                
                if freq[k] == i: res += 1
                
                for idx in range(v - l):
                    freq[cnt[s[idx]]] -= 1
                    cnt[s[idx]] -= 1
                    freq[cnt[s[idx]]] += 1

                    freq[cnt[s[idx+l]]] -= 1
                    cnt[s[idx+l]] += 1
                    freq[cnt[s[idx+l]]] += 1

                    if freq[k] == i: res += 1
            return res
        
        idx = 0
        ans = 0
        n = len(w)
        for i in range(1, n):
            if abs(ord(w[i]) - ord(w[i-1])) > 2:
                ans += calc(w[idx:i])
                idx = i
        ans += calc(w[idx:])
        return ans


class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        l = 0
        n = len(word)
        cc = defaultdict(deque)
        ans = 0
        def check():
            for ch, q in cc.items():
                if len(q) > k:
                    return False
            return True
        def calc():
            intervals = []
            reach = -1
            for ch, q in cc.items():
                if q:
                    intervals.append((q[0],q[-1]))
                    if len(q) < k:
                        reach = max(reach,q[-1])
            res = 0
            cur = -1
            intervals.sort()
            for mi, mx in intervals:
                if mi > cur and mi > reach:
                    res += 1
                cur = max(cur,mx)
            return res 

        for r in range(n):
            ch = word[r]
            cc[ch].append(r)
            while (l < r and r > 0 and abs(ord(word[r-1])-ord(word[r])) > 2) or not check():
                cc[word[l]].popleft()
                l += 1
            # print(l,r,cc,calc())
            ans += calc()
        return ans 