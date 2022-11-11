class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums.sort(key = lambda x: (x&1, x))
        target.sort(key = lambda x: (x&1, x))
        return sum(abs(a-b) for a, b in zip(nums, target))//4




class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums.sort(key = lambda x: (x&1, x))
        target.sort(key = lambda x: (x&1, x))
        delta, cnt = 0, 0
        for a, b in zip(nums, target):
            change = b-a
            if change == 0:
                continue
            if change*delta <= 0:
                cnt += abs(change)
                delta -= change
            else:
                if abs(delta) >= abs(change):
                    delta -= change
                else:
                    delta -= change
                    cnt += abs(delta)
        return cnt//2

