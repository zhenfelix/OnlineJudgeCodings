# class Solution:
#     def minInsertions(self, s: str) -> int:
#         s = s+'#'
#         cnt, left, right = 0, 0, 0
#         for ch in s:
#             if ch == '(' or ch == '#':
#                 if right > 0 or ch == '#':
#                     cnt += (right&1)
#                     left -= (right+1)//2
#                     if left < 0:
#                         cnt -= left
#                         left = 0
#                     right = 0
#                     if ch == '#':
#                         cnt += left*2
#                 left += 1
#             else:
#                 right += 1
#             # print(ch,left,right,cnt)
#         return cnt

# class Solution(object):
#     def minInsertions(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         left, right, cnt = 0, 0, 0
#         for ch in s+'#':
#             if ch in ['(','#']:
#                 if right > 0:
#                     need = (right+1)//2
#                     cnt += (right&1) + max(0,need-left)
#                     left, right = max(0,left-need), 0
#                 if ch == '#':
#                     cnt += 2*left
#                     continue
#                 left += 1
#             else:
#                 right += 1

#         return cnt


class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right, cnt = 0, 0, 0
        for ch in s+'#':
            if ch in ['(','#']:
                if right&1:
                    right += 1
                    cnt += 1
                need = right//2
                cnt += max(0,need-left)
                left, right = max(0,left-need), 0
                if ch == '#':
                    cnt += 2*left
                    continue
                left += 1
            else:
                right += 1

        return cnt
