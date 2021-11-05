# class Solution:
#     def nextGreaterElement(self, n: int) -> int:
#         cur = n
#         arr = [cur%10]
#         cur //= 10
#         while cur:
#             tmp = cur%10
#             if arr[-1] > tmp:
#                 idx = 0
#                 while arr[idx] <= cur%10:
#                     idx += 1
#                 arr[idx], tmp = tmp, arr[idx]
#                 cur = cur - arr[idx] + tmp
#                 res, base = 0, 1
#                 for a in arr:
#                     base *= 10
#                     res *= 10
#                     res += a
#                 res = cur*base + res
#                 if res > (1<<31)-1:
#                     return -1
#                 return res
#             else:
#                 arr.append(tmp)
#                 cur //= 10
            
#         return -1


# class Solution:
#     def nextGreaterElement(self, n: int) -> int:
#         s = str(n)
#         m = len(s)
#         st = []
#         for i in range(m)[::-1]:
#             idx = bisect.bisect_right(st,s[i])
#             # print(idx)
#             if idx == len(st):
#                 st.append(s[i])
#             else:
#                 ch = s[i]
#                 st[idx], ch = ch, st[idx]
#                 res = int(s[:i]+ch+''.join(st))
#                 return res if res <= (1<<31-1) else -1
#         return -1

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        m = len(nums)
        for i in range(m)[::-1]:
            if i < m-1 and nums[i] < nums[i+1]:
                j = i+1
                while j < m and nums[j] > nums[i]:
                    j += 1
                j -= 1
                nums[i], nums[j] = nums[j], nums[i]
                left, right = i+1, m-1
                while left < right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
                res = int(''.join(nums))
                return res if res < (1<<31) else -1
        return -1

class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = list(map(int, str(n)))
        i = len(s)-1
        while i-1>=0 and s[i]<=s[i-1]:
            i -= 1
            
        if i==0:
            return -1
        
        j = i
        while j+1<len(s) and s[j+1]>s[i-1]:
            j += 1
        
        s[i-1], s[j] = s[j], s[i-1]
        s[i:] = reversed(s[i:])
        ret = int(''.join(map(str, s)))
        
        return ret if ret<=((1<<31)-1) else -1