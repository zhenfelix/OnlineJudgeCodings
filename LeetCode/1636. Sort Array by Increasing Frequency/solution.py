class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cc = Counter(nums)
        # print(cc)
        return sorted(nums, key = lambda x: (cc[x],-x))