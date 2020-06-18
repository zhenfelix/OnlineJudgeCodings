# class Solution:
    # def minSumOfLengths(self, arr: List[int], target: int) -> int:
    #     res = float('inf')
    #     ends = [-1]
    #     mp = {-1:float('inf')}
    #     left, right, sums, n = 0, 0, 0, len(arr)
    #     cur = 0
    #     for right in range(n):
    #         sums += arr[right]
    #         while left < n and sums > target:
    #             sums -= arr[left]
    #             left += 1
    #             while cur+1 < len(ends) and left > ends[cur+1]:
    #                 cur += 1
    #         if sums == target:
    #             res = min(res, mp[ends[cur]]+right-left+1)
    #             if right-left+1 < mp[ends[-1]]:
    #                 ends.append(right)
    #                 mp[right] = right-left+1
    #             # print(ends,left,right,cur)
    #     return -1 if res == float('inf') else res
    
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefix = {0: -1}
        best_till = [math.inf] * len(arr)
        ans = best = math.inf
        for i, curr in enumerate(itertools.accumulate(arr)):
            if curr - target in prefix:
                end = prefix[curr - target]
                if end > -1:
                    ans = min(ans, i - end + best_till[end])
                best = min(best, i - end)
            best_till[i] = best
            prefix[curr] = i
        return -1 if ans == math.inf else ans

class Solution:
    def minSumOfLengths(self, a: List[int], targ: int) -> int:
        
        n = len(a)
        d1 = defaultdict(lambda: inf)
        ret2 = inf
        tot = 0
        j = 0
        
        for i,x in enumerate(a):
            
            tot += x
            
            while tot > targ:
                tot -= a[j]
                j += 1
            
            sz = i-j+1
            
            if tot == targ:
                d1[i] = sz
                ret2 = min(ret2, d1[j-1] + sz)
            
            d1[i] = min(d1[i], d1[i-1])
        
        return -1 if ret2 == inf else ret2