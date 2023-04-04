class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cc = Counter(nums)
        n = len(nums)
        nums = sorted([[v,k] for k, v in cc.items()],reverse = True)
        for _ in range(n):
            tmp = []
            for v, k in nums:
                if v <= len(ans):
                    break 
                tmp.append(k)
            if not tmp:
                break
            ans.append(tmp)
        return ans 


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cnt = Counter(nums)
        while cnt:
            ans.append(list(cnt))
            for x in ans[-1]:
                cnt[x] -= 1
                if cnt[x] == 0:
                    del cnt[x]
        return ans


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/convert-an-array-into-a-2d-array-with-conditions/solution/ha-xi-biao-mo-ni-by-endlesscheng-6rgb/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。