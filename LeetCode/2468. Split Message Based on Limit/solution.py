class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        n = len(message)
        def check(sz):
            ans = []
            cnt = 1
            cur = 0
            while cur < n:
                tmp = len(str(cnt))
                if tmp > sz:
                    return []
                delta = limit-tmp-sz-3
                if delta <= 0:
                    return []
                nxt = min(n,cur+delta)
                ans.append(message[cur:nxt]+'<'+str(cnt)+'/')
                cur = nxt
                cnt += 1
            cnt -= 1
            m = len(ans)
            suff = str(cnt)+'>'
            for i in range(m):
                ans[i] = ans[i]+suff
            return ans 
        for sz in range(1,6):
            candidate = check(sz)
            if candidate:
                return candidate
        return []
