class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        q = collections.deque()
        visited = set()
        q.append(id)
        visited.add(id)
        fs = []
        distance = 0
        while q and distance <= level:
            for _ in range(len(q)):
                cur = q.popleft()
                if distance == level:
                    fs.append(cur)
                for nxt in friends[cur]:
                    if nxt not in visited:
                        q.append(nxt)
                        visited.add(nxt)
            distance += 1
        mp = collections.Counter()
        for f in fs:
            for v in watchedVideos[f]:
                mp[v] += 1
        res = mp.keys()
        return sorted(res, key = lambda x: (mp[x],x))
