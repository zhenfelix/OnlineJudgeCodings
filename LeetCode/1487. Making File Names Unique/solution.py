class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        res = []
        seen = set()
        pos = defaultdict(int)
        for name in names:
            if name in seen:
                while True:
                    pos[name] += 1
                    if name + '('+str(pos[name])+')' not in seen:
                        name += '('+str(pos[name])+')'
                        break
            res.append(name)
            seen.add(name)
        return res
                 
