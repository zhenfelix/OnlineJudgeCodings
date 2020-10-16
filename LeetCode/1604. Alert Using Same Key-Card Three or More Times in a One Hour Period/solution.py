class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def convert(s):
            hh, mm = s.split(':')
            return int(hh)*60 + int(mm)
        mp = defaultdict(list)
        res = []
        for name, time in zip(keyName,keyTime):
            mp[name].append(convert(time))
        for k, v in mp.items():
            v.sort()
            for i, t in enumerate(v):
                if i < 2:
                    continue
                if v[i] - v[i-2] <= 60:
                    res.append(k)
                    break
        return sorted(res)
