# class Solution:
#     def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
#         ans, nums=0, 0
#         for x in zip(customers,grumpy):
#             if x[1]==0:
#                 nums+=x[0]
#         for i in range(X):
#             if grumpy[i]==1:
#                 nums+=customers[i]
#         ans = nums
#         for j in range(len(customers)-X):
#             if grumpy[j+X]==1:
#                 nums+=customers[j+X]
#             if grumpy[j]==1:
#                 nums-=customers[j]
#             ans = max(ans,nums)
#         return ans

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        window = 0
        satisfied = 0
        maxi = 0
        for i, customer in enumerate(customers):
            if grumpy[i]:
                window += customer
            else:
                satisfied += customer
            if i >= X:
                window -= grumpy[i-X] * customers[i-X]
            maxi = max(maxi, window)
        return satisfied + maxi