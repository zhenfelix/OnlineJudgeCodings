class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        cc = Counter(nums)
        arr = sorted([(-v,k) for k, v in cc.items()])
        for _, k in arr:
            if k%2 == 0:
                return k 
        return -1