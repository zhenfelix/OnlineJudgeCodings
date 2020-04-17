class Solution:
    # def sortByBits(self, arr: List[int]) -> List[int]:
    #     def bitcnt(num):
    #         cnt = 0
    #         while num:
    #             cnt += (num&1)
    #             num >>= 1
    #         return cnt
    #     return sorted(arr, key=lambda x: (bitcnt(x),x))
    
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))