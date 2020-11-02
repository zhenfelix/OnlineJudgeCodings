class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for left, right in zip(l,r):
            arr = sorted(nums[left:right+1])
            if all(arr[i]-arr[i-1] == arr[1]-arr[0] for i in range(1,len(arr))):
                res.append(True)
            else:
                res.append(False)
        return res