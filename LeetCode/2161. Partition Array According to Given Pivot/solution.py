class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less, great = [], []
        cnt = 0
        for x in nums:
            if x < pivot:
                less.append(x)
            elif x > pivot:
                great.append(x)
            else:
                cnt += 1
        return less+[pivot]*cnt+great