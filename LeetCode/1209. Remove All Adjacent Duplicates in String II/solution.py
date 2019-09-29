class Solution:
    def removeDuplicates(self, s, k):
        stack = [['#', 0]]
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return ''.join(c * k for c, k in stack)
        

# class Solution:
#     def removeDuplicates(self, s: str, k: int) -> str:
#         st = []
#         for ch in s:
#             if st and st[-1][-1] == ch:
#                 st.append((st[-1][0]+1,ch))
#             else:
#                 st.append((1,ch))
#             if st[-1][0] == k:
#                 for j in range(k):
#                     st.pop()
#         return ''.join([a[-1] for a in st])