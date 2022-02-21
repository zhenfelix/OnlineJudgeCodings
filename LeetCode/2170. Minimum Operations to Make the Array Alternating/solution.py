class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cc1, cc2 = Counter(), Counter()
        tot1, tot2 = 0, 0
        for i, x in enumerate(nums):
            if i&1:
                cc1[x] += 1 
                tot1 += 1
            else:
                cc2[x] += 1
                tot2 += 1
        arr1 = sorted([(v,k) for k, v in cc1.items()], reverse = True)
        arr2 = sorted([(v,k) for k, v in cc2.items()], reverse = True)
        arr1.append((0,float('inf')))
        arr1.append((0,float('inf')))
        arr2.append((0,float('inf')))
        arr2.append((0,float('inf')))
        # print(arr1,arr2)
        res = float('inf')
        # for x in nums:
        #     res = min(res, tot1-cc1[x]+(tot2-arr2[0][0] if x != arr2[0][1] else tot2-arr2[1][0]))
        #     res = min(res, tot2-cc2[x]+(tot1-arr1[0][0] if x != arr1[0][1] else tot1-arr1[1][0]))
        res = min(res, tot1-arr1[0][0]+(tot2-arr2[0][0] if arr1[0][1] != arr2[0][1] else tot2-arr2[1]
        [0]))
        res = min(res, tot2-arr2[0][0]+(tot1-arr1[0][0] if arr2[0][1] != arr1[0][1] else tot1-arr1[1]
        [0]))
        return res


from collections import Counter

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        ec = Counter(nums[::2])
        oc = Counter(nums[1::2])
        
        e = sorted([(ec[key], key) for key in ec], reverse=True)
        o = sorted([(oc[key], key) for key in oc], reverse=True)
        
        ans = n
        for i in range(min(2, len(e))):
            for j in range(min(2, len(o))):
                if e[i][1] != o[j][1]:
                    ans = min(ans, n - e[i][0] - o[j][0])
                else:
                    ans = min(ans, n - max(e[i][0], o[j][0]))
        
        return ans


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/oA57vT/view/OnnrrJ/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。