class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        mp = defaultdict(set)
        for uid, tid in logs:
            mp[uid].add(tid)
        cnt = Counter()
        for uid, tids in mp.items():
            cnt[len(tids)] += 1
        res = [0]*k
        for k, v in cnt.items():
            res[k-1] = v
        return res 