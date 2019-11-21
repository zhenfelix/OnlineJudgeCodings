import random
class Solution:

    def __init__(self, w: List[int]):
        n = len(w)
        for i in range(1,n):
            w[i] += w[i-1]
        self.w = w
        return

    def pickIndex(self) -> int:
        w = self.w
        n = len(w)
        p = random.randint(1,w[-1])
        left, right = 0, n-1
        while left <= right:
            mid = (left+right)//2
            if w[mid] >= p:
                right = mid - 1
            else:
                left = mid + 1
        return left

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


# class Solution:

#     def __init__(self, w):
#         self.w = list(itertools.accumulate(w))

#     def pickIndex(self):
#         return bisect.bisect_left(self.w, random.randint(1, self.w[-1]))