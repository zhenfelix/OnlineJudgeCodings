

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         res = 0
#         st = []
#         for i, h in enumerate(height):
#             pre_height = h
#             while len(st) > 0 and height[st[-1]] < h:
#                 idx = st.pop()
#                 res += (height[idx]-pre_height)*(i-idx-1)
#                 pre_height = height[idx]
                
#             if len(st) > 0:
#                 res += (h-pre_height)*(i-st[-1]-1)
            
#             st.append(i)
        
#         return res

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         n = len(height)
#         res = 0
#         left, right = list(range(n)), list(range(n))
#         for i in range(n):
#             if i > 0:
#                 if height[left[i-1]] > height[i]:
#                     left[i] = left[i-1]
#                 if height[right[n-i]] > height[n-1-i]:
#                     right[n-1-i] = right[n-i]
#         # print(left)
#         # print(right)
#         for i in range(n):
#             h = min(height[left[i]], height[right[i]])
#             if h > height[i]:
#                 res += (h-height[i])
                
#         return res

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         n = len(height)
#         res = 0
#         left, right = 0, n-1
#         leftMax, rightMax = 0, 0
#         while left < right:
#             leftMax = max(leftMax, height[left])
#             rightMax = max(rightMax, height[right])
#             if leftMax < rightMax:
#                 res += leftMax-height[left]
#                 left += 1
#             else:
#                 res += rightMax-height[right]
#                 right -= 1
                
#         return res

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         n = len(height)
#         res = 0
#         left, right = 0, n-1
#         leftMax, rightMax = 0, 0
#         while left < right:
#             if height[left] < height[right]:
#                 if height[left] > leftMax:
#                     leftMax = height[left]
#                 else:
#                     res += leftMax-height[left]
#                 left += 1
#             else:
#                 if height[right] > rightMax:
#                     rightMax = height[right]
#                 else:
#                     res += rightMax-height[right]
#                 right -= 1
                
#         return res
# Use Induction to prove the heigher bar between left and right index is the highest bar so far 
        

class Solution:
    def trap(self, height: List[int]) -> int:
        st = []
        sums = 0
        for i, h in enumerate(height):
            while st and height[st[-1]] < h:
                # 以cur为底部，找出左右两边比它大的位置
                # Next Greater Element I
                # Next Greater Element II
                cur = st.pop()
                if st:
                    sums += (i-st[-1]-1)*(min(h,height[st[-1]])-height[cur])
            st.append(i)
        return sums

        


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        left, right = 0, n-1
        H = 0
        while left < right:
            if height[left] < height[right]:
                H = max(H, height[left])
                res += H-height[left]
                left += 1
            else:
                H = max(H, height[right]) 
                res += H-height[right]
                right -= 1
                
        return res
# this method could be generalized to 2D case    