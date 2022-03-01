# class Solution:
#     def isPossibleDivide(self, nums: List[int], k: int) -> bool:
#         n=len(nums)
#         if n%k:
#             return False
#         nums.sort()
#         cnt=collections.Counter(nums)
#         idx = 0
#         st=nums[idx]
#         while len(cnt)>0:
#             ntime=cnt[st]
#             idx += ntime*k
#             nst=float("inf")
#             for num in range(st,st+k):
#                 if cnt[num]<ntime:
#                     return False
#                 elif cnt[num]==ntime:
#                     cnt.pop(num)
#                 else:
#                     cnt[num]-=ntime
#                     nst = min(nst,num)
#             if nst==float("inf") and idx < n:
#                 nst=nums[idx]
#             st=nst
#         return True




# class Solution:
#     def isPossibleDivide(self, nums: List[int], k: int) -> bool:
#         n=len(nums)
#         if n%k:
#             return False
#         cnt=collections.Counter(nums)
#         st=min(cnt)
#         while len(cnt)>0:
#             ntime=cnt[st]
#             nst=-1
#             for num in range(st,st+k):
#                 if cnt[num]<ntime:
#                     return False
#                 elif cnt[num]==ntime:
#                     cnt.pop(num)
#                 else:
#                     cnt[num]-=ntime
#                     if nst<0:
#                         nst=num
#             if nst<0 and len(cnt)>0:
#                 nst=min(cnt)
#             st=nst
#         return True


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums)%k:
            return False
        cc = Counter(nums)
        for x in sorted(nums):
            if cc[x]:
                for y in range(x,x+k):
                    cc[y] -= 1
                    if cc[y] < 0:
                        return False
        return True

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        cc = collections.Counter(nums)
        for num in nums:
            if not cc[num]:
                continue
            for i in range(k):
                cc[num+i] -= 1
                if cc[num+i] < 0:
                    return False
        return True


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        end = collections.defaultdict(list)
        for num in nums:
            if end[num-1]:
                end[num].append(end[num-1].pop()+1)
            else:
                end[num].append(1)
            if end[num][-1] == k:
                end[num].pop()
            # print(end)
        if any(v for _,v in end.items()):
            return False

        return True


import collections
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count=collections.Counter(nums)
        keys=sorted(count.keys())
        for n in keys:
            if count[n]>0:
                minus=count[n]
                for i in range(n,n+k):
                    if count[i]<minus:
                        return False
                    count[i]-=minus
        return True