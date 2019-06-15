# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         n = len(heights)
#         st = []
#         left = [0]*n
#         st.append(0)
#         for i in range(1,n):
#             tmp = i
#             while len(st)>0 and heights[i]<=heights[st[-1]]:
#                 tmp = left[st[-1]]
#                 st.pop()
#             left[i] = tmp
#             st.append(i)
            
#         st = []
#         right = [n]*n
#         st.append(n)
#         for j in range(n-1,0,-1):
#             tmp = j
#             while len(st)>0 and heights[j-1]<=heights[st[-1]-1]:
#                 tmp = right[st[-1]-1]
#                 st.pop()
#             right[j-1] = tmp
#             st.append(j)
            
#         ans = 0
#         for idx in range(n):
#             ans = max(ans, (right[idx]-left[idx])*heights[idx])
            
#         return ans
                

class Solution:
    def largestRectangleArea(self, height):
        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1 #already pop out
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans
    
    
# This idea is really beautiful. However I felt a bit confused when reading the explanation. After thinking for a while, here is my thought if it is helpful. For any bar x, if it's in a rectangle of which the height is also the height of x, we know that every bar in the rectangle must be no shorter than x. Then the issue is to find the left and right boundary where the bars are shorter than x. According to the code, when a bar is popped out from the stack, we know it must be higher than the bar at position i, so bar[i] must be the right boundary (exclusive) of the rectangle, and the previous bar in the stack is the first one that is shorter than the popped one so it must be the left boundary (also exclusive). Then we find the rectangle.

