class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mp = {v: i+1 for i, v in enumerate(sorted(list(set(nums))))}
        m = len(mp)
        arr1, arr2 = [nums[0]], [nums[1]]
        tree1, tree2 = [0]*(m+1), [0]*(m+1)
        def update(idx, x, tree):
            while idx <= m:
                tree[idx] += x 
                idx += (idx&-idx)
            return
        def query(idx, tree):
            tmp = 0 
            while idx:
                tmp += tree[idx]
                idx -= (idx&-idx)
            return tmp 
        update(mp[nums[0]],1,tree1)
        update(mp[nums[1]],1,tree2)
        for i in range(2,n):
            v = nums[i]
            c1 = len(arr1)-query(mp[v],tree1)
            c2 = len(arr2)-query(mp[v],tree2)
            if c1 > c2:
                arr1.append(v)
                update(mp[v],1,tree1)
            elif c1 < c2:
                arr2.append(v)
                update(mp[v],1,tree2)
            else:
                if len(arr1) <= len(arr2):
                    arr1.append(v)
                    update(mp[v],1,tree1)
                else:
                    arr2.append(v)
                    update(mp[v],1,tree2)
        return arr1+arr2



class Fenwick:
    __slots__ = 'tree'

    def __init__(self, n: int):
        self.tree = [0] * n

    # 把下标为 i 的元素增加 1
    def add(self, i: int) -> None:
        while i < len(self.tree):
            self.tree[i] += 1
            i += i & -i

    # 返回下标在 [1,i] 的元素之和
    def pre(self, i: int) -> int:
        res = 0
        while i > 0:
            res += self.tree[i]
            i &= i - 1
        return res

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(set(nums))
        m = len(sorted_nums)
        a = [nums[0]]
        b = [nums[1]]
        t1 = Fenwick(m + 1)
        t2 = Fenwick(m + 1)
        t1.add(bisect_left(sorted_nums, nums[0]) + 1)
        t2.add(bisect_left(sorted_nums, nums[1]) + 1)
        for x in nums[2:]:
            v = bisect_left(sorted_nums, x) + 1
            gc1 = len(a) - t1.pre(v)  # greaterCount(a, v)
            gc2 = len(b) - t2.pre(v)  # greaterCount(b, v)
            if gc1 > gc2 or gc1 == gc2 and len(a) <= len(b):
                a.append(x)
                t1.add(v)
            else:
                b.append(x)
                t2.add(v)
        return a + b

作者：灵茶山艾府
链接：https://leetcode.cn/problems/distribute-elements-into-two-arrays-ii/solutions/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


from sortedcontainers import SortedList

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        def greaterCount(arr, val):
            return len(arr) - arr.bisect_right(val)

        arr1, arr2 = SortedList([nums[0]]), SortedList([nums[1]])
        res1, res2 = [nums[0]], [nums[1]]
        for i in range(2, len(nums)):
            c1, c2 = greaterCount(arr1, nums[i]), greaterCount(arr2, nums[i])
            if c1 > c2 or (c1 == c2 and len(arr1) <= len(arr2)):
                arr1.add(nums[i])
                res1.append(nums[i])
            else:
                arr2.add(nums[i])
                res2.append(nums[i])
        return res1 + res2


作者：TsReaper
链接：https://leetcode.cn/circle/discuss/ngeWpk/view/TIkw3s/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。