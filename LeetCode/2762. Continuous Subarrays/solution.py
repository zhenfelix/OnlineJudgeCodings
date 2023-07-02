class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        j = 0
        ans = 0
        mx = deque()
        mi = deque()
        for i in range(n):
            while mx and nums[mx[-1]] <= nums[i]:
                mx.pop()
            mx.append(i)
            while mi and nums[mi[-1]] >= nums[i]:
                mi.pop()
            mi.append(i)
            while nums[mx[0]]-nums[mi[0]] > 2:
                j += 1
                if mx[0] < j:
                    mx.popleft()
                if mi[0] < j:
                    mi.popleft()
            # print(j,i)
            ans += i-j+1
        return ans 

class Solution:
    def continuousSubarrays(self, a: List[int]) -> int:
        h = Counter()
        mo = deque([])
        ans = 0
        for i in a:
            mo.append(i)
            h[i] += 1
            while h[i-2]+h[i-1]+h[i]+h[i+1]+h[i+2] != len(mo):
                h[mo.popleft()] -= 1
            ans += len(mo)
        return ans