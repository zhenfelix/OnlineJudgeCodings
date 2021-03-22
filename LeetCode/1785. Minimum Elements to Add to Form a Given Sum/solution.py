class Solution:
    def minElements(self, A, limit, goal):
        return (abs(sum(A) - goal) + limit - 1) // limit        


# class Solution:
#     def minElements(self, nums: List[int], limit: int, goal: int) -> int:
#         delta = abs(goal-sum(nums))
#         if delta == 0:
#             return 0
#         return (delta-1)//limit + 1