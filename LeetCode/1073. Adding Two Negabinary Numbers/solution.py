class Solution:
    # def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
    #     n1, n2 = len(arr1), len(arr2)
    #     # if n1 < n2:
    #     #     arr1, arr2 = arr2, arr1
    #     #     n1, n2 = n2, n1
    #     i, j = n1-1, n2-1
    #     carry = 0
    #     res = []
    #     while i >= 0 or j >= 0 or carry != 0:
    #         a, b, cur = arr1[i] if i >= 0 else 0, arr2[j] if j >= 0 else 0, 0
    #         cur = a+b+carry
    #         cur, carry = cur%2, -1*(cur-cur%2)//2
    #         res.append(cur)
    #         i -= 1
    #         j -= 1
    #     # i = 0
    #     # while i < n1 and arr1[i] == 0:
    #     #     i += 1
    #     while res and res[-1] == 0:
    #         res.pop()
    #     return res[::-1] or [0]
    
    
    def addBinary(self, A, B):
        res = []
        carry = 0
        while A or B or carry:
            carry += (A or [0]).pop() + (B or [0]).pop()
            res.append(carry & 1)
            carry = carry >> 1
        return res[::-1]

    def addNegabinary(self, A, B):
        res = []
        carry = 0
        while A or B or carry:
            carry += (A or [0]).pop() + (B or [0]).pop()
            res.append(carry & 1)
            carry = -(carry >> 1)
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return res[::-1]
