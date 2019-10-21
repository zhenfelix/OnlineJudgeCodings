
from collections import Counter
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        left = mid = cnt = cnt_mid = ans = 0
        cc, cc_mid =Counter(), Counter()
        for right in range(len(A)):
            a = A[right]
            if cc[a] == 0:
                cnt += 1
            if cc_mid[a] == 0:
                cnt_mid += 1
            cc[a] += 1
            cc_mid[a] += 1
            if cnt > K:
                cnt = cnt_mid
                # cc = cc_mid.copy()
                # left = mid 
                while left < mid:
                    cc[A[left]] -= 1
                    left += 1
            while cnt_mid == K:
                a = A[mid]
                cc_mid[a] -= 1
                if cc_mid[a] == 0:
                    cnt_mid -= 1
                mid += 1
            ans += mid-left
                
        return ans



    # def subarraysWithKDistinct(self, A, K):
    #     return self.atMostK(A, K) - self.atMostK(A, K - 1)

    # def atMostK(self, A, K):
    #     count = collections.Counter()
    #     res = i = 0
    #     for j in range(len(A)):
    #         if count[A[j]] == 0: K -= 1
    #         count[A[j]] += 1
    #         while K < 0:
    #             count[A[i]] -= 1
    #             if count[A[i]] == 0: K += 1
    #             i += 1
    #         res += j - i + 1
    #     return res