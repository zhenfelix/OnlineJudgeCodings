class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cc = Counter(arr)
        nums = [v for v in cc]
        nums.sort(key=lambda x: cc[x])
        cnt = 0
        for v in nums:
            k -= cc[v]
            if k < 0:
                break
            cnt += 1
        return len(nums)-cnt


class Solution:
    def findMinNumDistinctIds(self, arr: List[int], k: int) -> int:
        pool = sorted(collections.Counter(arr).values(), reverse = True)
        while k:
            if k < pool[-1]:
                break
            k -= pool.pop()
        return len(pool)