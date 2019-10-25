class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        res, left = 0, 0
        for i, ch in enumerate(S):
            if ch == '(':
                left += 1
            else:
                left -= 1
                if S[i-1] == '(':
                    res += 2**left
        return res

# class Solution(object):
#     def scoreOfParentheses(self, S):
#         stack = [0] #The score of the current frame

#         for x in S:
#             if x == '(':
#                 stack.append(0)
#             else:
#                 v = stack.pop()
#                 stack[-1] += max(2 * v, 1)

#         return stack.pop()