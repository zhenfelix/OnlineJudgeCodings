from collections import defaultdict, Counter, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        n = len(words)
        mp = defaultdict(set)
        alphabet = set(words[0])
        for i in range(n-1):
            a, b = words[i], words[i+1]
            m = min(len(a), len(b))
            j = 0
            while j < m and a[j] == b[j]:
                j += 1
            if j < m:
                mp[a[j]].add(b[j])
            alphabet = alphabet.union(set(words[i+1]))
            # print(set(words[i+1]), alphabet)
            
        res = ""
        cc = Counter()
        for key in mp:
            for ch in mp[key]:
                cc[ch] += 1
        pq = deque()
        # print(alphabet)
        for ch in alphabet:
            if cc[ch] == 0:
                pq.append(ch)
        while pq:
            ch = pq.popleft()
            res += ch
            for nxt in mp[ch]:
                cc[nxt] -= 1
                if cc[nxt] == 0:
                    pq.append(nxt)
        if len(res) < len(alphabet):
            return ""
        return res
        
        
        