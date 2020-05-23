class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        small = set(small)
        left, right, cnt, sz = 0, 0, defaultdict(int), 0
        res = [-float('inf'), float('inf')]
        while right < len(big):
            if big[right] in small:
                if cnt[big[right]] == 0:
                    sz += 1
                cnt[big[right]] += 1
            while sz == len(small):
                if right-left < res[-1]-res[0]:
                    res = [left,right]
                cnt[big[left]] -= 1
                if cnt[big[left]] == 0:
                    sz -= 1
                left += 1
            right += 1
        return res if res[-1] != float('inf') else []