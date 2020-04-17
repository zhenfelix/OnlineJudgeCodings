class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)
        cnt = defaultdict(int)
        n = len(arr)
        for i in range(n)[::-1]:
            cnt[arr[i]] = i
        return list(map(lambda x: cnt[x],nums))