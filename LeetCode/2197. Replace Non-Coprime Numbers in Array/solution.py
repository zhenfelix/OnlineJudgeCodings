class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [i for i in range(n)]
        right = [i for i in range(n)]
        # valid = [False]*(n-1) 
        edges = [1]*(n-1)
        q = deque()
        for i in range(1,n):
            g = gcd(nums[i-1],nums[i])
            if g > 1:
                q.append(i-1)
                edges[i-1] = g
                # valid[i-1] = True
        while q:
            i = q.popleft()
            g = edges[i]
            l, r = left[i], right[i+1]
            right[l] = r 
            left[r] = l 
            nums[l] = nums[l]*nums[i+1]//g
            if r+1 < n:
                g = gcd(nums[l],nums[r+1])
                if edges[r] == 1 and g > 1:
                    q.append(r)
                edges[r] = g 
            if l-1 >= 0:
                g = gcd(nums[left[l-1]],nums[l])
                if edges[l-1] == 1 and g > 1:
                    q.append(l-1)
                edges[l-1] = g 
        return [nums[i] for i in range(n) if left[right[i]] == i]


证明方法： 假设一个区间的合并过程存在一个序列，找出该最后被合并的边，然后可以用该边可以划分区间成左右两部分，从而把序列也分成两个子序列分别考虑
from math import gcd, lcm

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            ans.append(num)
            while len(ans) >= 2 and gcd(ans[-2], ans[-1]) > 1:
                r = ans.pop()
                ans[-1] = lcm(ans[-1], r)
            
        return ans

作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/c8HUDh/view/eCf0rc/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。