class Solution:
    def removeKdigits(self, s: str, k: int) -> str:
        n = len(s)
        k = n-k
        q = deque()
        res = []
        for i, ch in enumerate(s):
            while q and s[q[-1]] > ch:
                q.pop()
            q.append(i)
            if n-i == k:
                j = q.popleft()
                if res or s[j] != '0':
                    res.append(s[j])
                k -= 1
        return ''.join(res) if res else '0'



class Solution:
    def removeKdigits(self, nums, k):
        st = []
        for num in nums:
            while k and st and st[-1] > num:
                st.pop()
                k -= 1
            st.append(num)
        return ''.join(st[:-k or None]).lstrip('0') or '0'