class Solution:
#     def sumSubarrayMins(self, arr: List[int]) -> int:
#         MOD = 10**9+7
#         res = 0
#         n = len(arr)
#         right = [n for i in range(n)]
#         st = []
#         for i in range(n)[::-1]:
#             while st and arr[st[-1]] > arr[i]:
#                 st.pop()
#             if st:
#                 right[i] = st[-1]
#             st.append(i)
#         st = []
#         for i in range(n):
#             while st and arr[st[-1]] >= arr[i]:
#                 st.pop()
#             cnt = i-st[-1] if st else i+1
#             # print(i,cnt,right[i]-i,arr[i])
#             res += cnt*(right[i]-i)*arr[i]
#             res %= MOD
#             st.append(i)
#         return res


    def sumSubarrayMins(self, A):
        res = 0
        s = []
        A = [0] + A + [0]
        for i, x in enumerate(A):
            while s and A[s[-1]] > x:
                j = s.pop()
                k = s[-1]
                res += A[j] * (i - j) * (j - k)
            s.append(i)
        return res % (10**9 + 7)



class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        st, sums = [(-float("inf"),-1,0)], 0
        for i, a in enumerate(A):
            while st[-1][0] > a:
                st.pop()
            val, idx, postsum = st[-1]
            postsum += a*(i-idx)
            sums += postsum
            st.append((a,i,postsum))
        return sums%(10**9+7)