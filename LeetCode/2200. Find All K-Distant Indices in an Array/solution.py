class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            for j in range(max(0,i-k),min(n,i+k+1)):
                if nums[j] == key:
                    res.append(i)
                    break
        return res


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        positions = []
        n = len(nums)
        for i, v in enumerate(nums):
            if v == key:
                positions.append(i)
        cur = 0
        res = []
        for i in range(n):
            if cur < len(positions) and i > positions[cur]:
                cur += 1
            if (cur-1 >= 0 and positions[cur-1] >= i-k) or (cur < len(positions) and positions[cur] <= i+k):
                res.append(i)
        return res


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        good = [False] * n
        last_key = -1
        for i in range(n):
            if nums[i] == key:
                last_key = i
            if last_key != -1 and i - last_key <= k:
                good[i] = True
        last_key = -1
        for i in range(n - 1, -1, -1):
            if nums[i] == key:
                last_key = i
            if last_key != -1 and last_key - i <= k:
                good[i] = True
        return [i for i in range(n) if good[i]]    


# 作者：吴自华
# 链接：https://leetcode-cn.com/circle/discuss/3PMerp/view/yboIva/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。