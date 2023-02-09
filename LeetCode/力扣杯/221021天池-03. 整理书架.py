class Solution:
    def arrangeBookshelf(self, order: List[int], limit: int) -> List[int]:
        tot = Counter(order)
        cnt = Counter()
        st = []
        for ch in order:
            if cnt[ch] == limit:
                tot[ch] -= 1
                continue
            while st and st[-1] > ch and tot[st[-1]] > limit:
                tot[st[-1]] -= 1
                cnt[st[-1]] -= 1
                st.pop()
            st.append(ch)
            cnt[ch] += 1

        return st 



class Solution:
    def arrangeBookshelf(self, order: List[int], limit: int) -> List[int]:
        cc = Counter(order)
        cnt = Counter()
        res = []
        hq = []
        cur = -1
        for i, ch in enumerate(order):
            heapq.heappush(hq, (ch,i))
            cc[ch] -= 1
            if cc[ch] < limit:
                while hq:
                    nch, j = heappop(hq)
                    if nch <= ch and cnt[nch] < limit and j > cur:
                        cur = j
                        res.append(nch)
                        cc[nch] += 1
                        cnt[nch] += 1
                        if nch == ch:
                            break
        while hq:
            ch, i = heappop(hq)
            if cnt[ch] < limit and i > cur:
                cur = i 
                res.append(ch)
                cnt[ch] += 1
        return res 
