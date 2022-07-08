class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        prefix = defaultdict(list)
        suffix = defaultdict(set)
        n = len(ideas)
        for s in ideas:
            prefix[s[0]].append(s)
            suffix[s[1:]].add(s[0])
        # print(prefix)
        # print(suffix)
        ans = 0
        for ch, ss in prefix.items():
            cc = Counter()
            for s in ss:
                for ch2 in suffix[s[1:]]:
                    cc[ch2] += 1
            for s in ss:
                for ch2 in prefix.keys():
                    if ch2 in suffix[s[1:]]:
                        continue
                    ans += len(prefix[ch2])-cc[ch2]
        return ans



class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        seen = set(ideas)
        cnt = defaultdict(int)
        ans = 0
        for s in ideas:
            x = s[0]
            for i in range(26):
                y = chr(ord('a')+i)
                if y+s[1:] not in seen:
                    cnt[(x,y)] += 1
        for s in ideas:
            x = s[0]
            for i in range(26):
                y = chr(ord('a')+i)
                if y+s[1:] not in seen:
                    ans += cnt[(y,x)]
        return ans