class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.mp = Counter(nums2)


    def add(self, index: int, val: int) -> None:
        self.mp[self.nums2[index]] -= 1
        self.mp[self.nums2[index]+val] += 1
        self.nums2[index] += val


    def count(self, tot: int) -> int:
        res = 0
        for x in self.nums1:
            res += self.mp[tot-x]
        return res



# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)