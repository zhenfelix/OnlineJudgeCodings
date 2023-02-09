class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = [x-1 for x in nums1]
        nums2 = [x-1 for x in nums2]
        n = len(nums1)
        cc = [0]*n 
        candidates = []
        cost = 0
        for i in range(n):
            if nums1[i] != nums2[i]:
                candidates.append(i)
            else:
                cc[nums1[i]] += 1 
                cost += i 
        tot = sum(cc)
        mx = max(cc)
        # print(cc,candidates)
        if mx > tot-mx:
            plus = mx-(tot-mx)
            idx = -1
            for i in range(n):
                if cc[i] == mx:
                    idx = i 
                    break 
            for i in candidates:
                if nums1[i] != idx and nums2[i] != idx:
                    cost += i 
                    plus -= 1
                    if plus <= 0:
                        break
            if plus > 0:
                return -1
            return cost 
        # elif tot&1:
        #     delta = inf
        #     for i in candidates:
        #         if tot-cc[nums1[i]]-cc[nums2[i]] > 0:
        #             delta = min(delta,i)
        #             break
        #     for i in range(n):
        #         if nums1[i] == nums2[i]:
        #             delta = min(delta,i)
        #             break
        #     return cost
        return cost