class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cc = Counter(arr)
        arr = [k for k,v in cc.items() if k==v]
        arr = sorted(arr, key=lambda x:-x)
        return arr[0] if arr else -1
        