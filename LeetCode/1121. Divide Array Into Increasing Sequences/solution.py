from collections import Counter
class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], K: int) -> bool:
        cc = Counter(nums)
        # print(cc)
        return K*max(cc.values()) <= len(nums)


# Think in the frequency of the numbers and how this affects the number of sequences needed.

# What is the minimum number of sequences we need to form? Considering frequency of the numbers.

# Think about the least number of sequences to maximize the lengths.

# The number of sequences needed is equal to the maximum frequency of an element.

# How to put the other elements into sequences ? Think in a greedy approach.