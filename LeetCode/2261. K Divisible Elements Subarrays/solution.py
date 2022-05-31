# 字典树
class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        s, n = set(), len(nums)
        root = dict()
        res = 0
        for i in range(n):
            cnt = 0
            cur = root
            for j in range(i, n):
                if nums[j] % p == 0:
                    cnt += 1
                    if cnt > k:
                        break
                if nums[j] not in cur:
                    cur[nums[j]] = dict()
                    res += 1
                cur = cur[nums[j]]
        return res


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        seen = set()
        left, cnt = 0, 0
        n = len(nums)
        for right in range(n):
            if nums[right]%p == 0:
                cnt += 1
            while cnt > k:
                if nums[left]%p == 0:
                    cnt -= 1
                left += 1
            for i in range(left,right+1):
                s = '*'.join(map(str,nums[i:right+1]))
                if s not in seen:
                    seen.add(s)
        return len(seen)


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        s, n = set(), len(nums)
        for i in range(n):
            cnt = 0
            for j in range(i, n):
                if nums[j] % p == 0:
                    cnt += 1
                    if cnt > k:
                        break
                s.add(tuple(nums[i: j + 1]))
        return len(s)


# 作者：endlesscheng
# 链接：https://leetcode-cn.com/problems/k-divisible-elements-subarrays/solution/ha-xi-biao-mo-ni-by-endlesscheng-wrc7/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        seen = set()
        left, cnt = 0, 0
        n = len(nums)
        for right in range(n):
            if nums[right]%p == 0:
                cnt += 1
            while cnt > k:
                if nums[left]%p == 0:
                    cnt -= 1
                left += 1
            for i in range(left,right+1):
                # if tuple(nums[i:right+1]) in seen:
                #     break
                seen.add(tuple(nums[i:right+1]))
        return len(seen)


