# 1. We can always find an equivalent solution in ascending order of course's end time.

#   Assuming we have found a solution, whose sequence is "b...a...", where "b" is the first one and "a" is the one with the earliest end time. We can safely switch the order of "a" and "b" and the solution "a...b..." still holds, because "t_b < t_a <= e_a <= e_b" where t_i stands for time after finishing course i and e_i stands for end time of course i, and then "t_a < t_b <= e_a <= e_b" still holds after switching. By applying the argument recursively we conclude there is always an equivalent solution in ascending order of course's end time, therefore we can focus on wheather course i exists in the solution instead of their orders if we sorted the courses by ascending end time. In this step, we have dramatically reduced the search space from n! permutaions to 2^n combinations, furthere more, this problem is similar to knapsack problem which could be optimized by dynamic programming.
# ```
# class Solution:
#     def scheduleCourse(self, courses: List[List[int]]) -> int:
#         courses = sorted(courses, key=lambda x: x[1])
#         n = len(courses)
#         memo = {}
#         def dfs(idx, start):
#             if (idx, start) in memo:
#                 return memo[idx, start]
#             if idx == n or start > courses[-1][1]:
#                 return 0
#             ans = 0
#             if start+courses[idx][0] <= courses[idx][1]:
#                 ans = max(ans, 1+dfs(idx+1, start+courses[idx][0]))
#             ans = max(ans, dfs(idx+1,start))
#             memo[idx,start] = ans
#             return ans
#         return dfs(0,0)
# ```

# 2. After sorted by ascending end time, let "dp[k]=n" stands for the optimal solution for the first k courses [0,1...,k-1,k] and has the earliest finishing time, while the maximum number of courses taken is our first priority. At the k+1 course, we have two possibilities:

#   i.  Taking the k+1 th course will not go beyond its end time, we can safely add the k+1 th course to our solution, and "dp[k+1]=n+1" is guaranteed to be the optimal solution for the first k+1 courses and has the earliest finishing time
#   ii. Taking the k+1 th course is illegal, we can replace the course whose duration is smaller (the smallest among the solution "dp[k]=n" ) than the k+1 th course, otherwise discard the k+1 th course, which implies n smallest duration courses among all first k+1 courses, and thus the earliest finishing time for n courses in k+1 courses, "dp[k+1]=n" still holds for k+1.
#   extra: If we had "dp'[k]=n-1" and finishing time is earlier which could guaranteen we add the k+1 th course to our solution, then we have "dp'[k+1]=n". But wait a moment, its finishing time could not be earlier than the n smallest duration courses chosen, therefore we only need to consider the above two possibilities.
    
# ```
# import heapq
# class Solution:
#     def scheduleCourse(self, courses: List[List[int]]) -> int:
#         courses = sorted(courses, key=lambda x: x[1])
#         n = len(courses)
#         dp = []
#         start = 0
#         for course in courses:
#             heapq.heappush(dp, -course[0])
#             start += course[0]
#             if start > course[1]:
#                 start += heapq.heappop(dp)
#         return len(dp)
# ```

import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses, key=lambda x: x[1])
        n = len(courses)
        dp = []
        start = 0
        for course in courses:
            heapq.heappush(dp, -course[0])
            start += course[0]
            if start > course[1]:
                start += heapq.heappop(dp)
        return len(dp)
        
        
        
    
            