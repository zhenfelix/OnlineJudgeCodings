# class Solution:
#     def subSort(self, array: List[int]) -> List[int]:
#         array2 = sorted(array)
#         n = len(array)
#         i, j = 0, n-1
#         while i < n and array[i] == array2[i]:
#             i += 1
#         while j >= 0 and array[j] == array2[j]:
#             j -= 1
#         return [i,j] if i <= j else [-1,-1]

class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        n = len(array)
        big, small = -float('inf'), float('inf')
        j, i = -1, -1
        for k in range(n):
            a = array[k]
            if a < big:
                j = k
            big = max(big,a)
        for k in range(n)[::-1]:
            a = array[k]
            if a > small:
                i = k
            small = min(small,a)
        return [i,j]