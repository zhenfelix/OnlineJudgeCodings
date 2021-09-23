class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        cc = Counter(s)
        q = deque()
        alphas = [chr(ord('a')+i) for i in range(26)]

        def check(pattern):
            m = len(pattern)
            i, cnt = 0, 0
            for ch in s:
                if ch == pattern[i]:
                    i += 1
                if i == m:
                    cnt += 1
                    i = 0
            return cnt



        for ch in alphas:
            if cc[ch] >= k:
                q.append(ch)
        while q:
            cur = q.popleft()
            for ch in cur:
                cc[ch] -= k
            for ch in alphas:
                if cc[ch] >= k:
                    if check(cur+ch) >= k:
                        q.append(cur+ch)
            for ch in cur:
                cc[ch] += k
            if not q:
                return cur
        return ""
