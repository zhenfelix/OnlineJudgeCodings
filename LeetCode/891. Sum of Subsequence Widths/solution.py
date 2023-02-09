class Solution:
    # def sumSubseqWidths(self, A: List[int]) -> int:
    #     A = sorted(A)
    #     total, cur, cnt = 0, 0, 0
    #     MOD = 10**9 + 7
    #     for i in range(1,len(A)):
    #         cnt *= 2
    #         cnt += 1
    #         cur *= 2
    #         cur += (A[i]-A[i-1])*cnt
    #         cur %= MOD
    #         total += cur
    #         total %= MOD
    #         # print(cur,cnt)
    #     return total

    
    def sumSubseqWidths(self, A):
        return sum(((1 << i) - (1 << len(A) - i - 1)) * a for i, a in enumerate(sorted(A))) % (10**9 + 7)



# subarray solution
# class Solution:
#     def sumSubseqWidths(self, nums: List[int]) -> int:
#         MOD = 10**9+7
#         nums.append(0)
#         n = len(nums)
#         st = [-1]
#         mi = 0
#         for i in range(n):
#             while st and nums[st[-1]] >= nums[i]:
#                 j = st.pop()
#                 if j == -1:
#                     break
#                 mi = (mi+(j-st[-1])*(i-j)*nums[j])%MOD
#                 print(j,nums[j],(j-st[-1])*(i-j))
#             st.append(i)
#         nums[-1] = float('inf')
#         st = [-1]
#         mx = 0
#         for i in range(n):
#             while st and nums[st[-1]] <= nums[i]:
#                 j = st.pop()
#                 if j == -1:
#                     break
#                 print(j,nums[j],(j-st[-1])*(i-j))
#                 mx = (mx+(j-st[-1])*(i-j)*nums[j])%MOD
#             st.append(i)
#         return (mx+MOD-mi)%MOD


class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10**9+7
        nums.sort()
        n = len(nums)
        ans = 0
        f = [1]*(n+1)
        for i in range(1,n+1):
            f[i] = (f[i-1]*2)%MOD
        for i in range(i):
            ans = (ans+nums[i]*(f[i]+MOD-f[n-1-i]))%MOD
        return ans
