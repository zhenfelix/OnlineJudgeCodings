class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        arr = [bottom-1]+sorted(special)+[top+1]
        return max(b-a-1 for a, b in zip(arr[:-1],arr[1:]))