class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums[:]
        self.origin = nums[:]
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.origin

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        res = self.arr
        for i in range(len(res)):
            j = random.randrange(i+1)
            res[i], res[j] = res[j], res[i]
        return res
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()