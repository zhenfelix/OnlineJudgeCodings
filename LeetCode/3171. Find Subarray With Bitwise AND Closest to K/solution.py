class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = inf
        for i, x in enumerate(nums):
            ans = min(ans, abs(x - k))
            j = i - 1
            while j >= 0 and nums[j] & x != nums[j]:
                nums[j] &= x
                ans = min(ans, abs(nums[j] - k))
                j -= 1
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/find-subarray-with-bitwise-and-closest-to-k/solutions/2798206/li-yong-and-de-xing-zhi-pythonjavacgo-by-gg4d/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class StackQ:
    def __init__(self):
        self.st = []
        self.left = []
        self.right = []
        self.mask = (1<<32)-1
    def push(self, val):
        self.st.append(val)
        if self.right:
            val &= self.right[-1]            
        self.right.append(val)
    def pop(self):
        # print(self.st,self.left,self.right)
        if not self.left:
            self.left.append(self.st.pop())
            self.right.pop()
            while self.st:
                self.left.append(self.left[-1]&self.st.pop())
                self.right.pop()
        self.left.pop()
    def get(self):
        l = self.left[-1] if self.left else self.mask
        r = self.right[-1] if self.right else self.mask
        return l&r  
    def empty(self):
        return (not self.left) and (not self.right)

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = inf 
        n = len(nums)
        q = StackQ()
        j = 0
        for i in range(n):
            # print(i)
            q.push(nums[i])
            while not q.empty() and q.get() < k:
                ans = min(ans,abs(k-q.get()))
                q.pop()
            ans = min(ans,abs(k-q.get()))
        return ans 