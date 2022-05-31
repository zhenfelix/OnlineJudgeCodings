class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        flowers.sort()
        m = 0
        while flowers and flowers[-1] >= target:
            flowers.pop()
            m += 1
        ans = m*full
        n = len(flowers)
        if n == 0:
            return ans
        presums = [0]*n
        for i in range(n):
            presums[i] = presums[i-1]+flowers[i]
        if target*n-presums[n-1] <= newFlowers:
            ans += n*full
        # print(flowers)
        # print(newFlowers)
        left = right = 0
        for t in range(flowers[0],target):
            while left < n and flowers[left] <= t:
                left += 1
            if t*left-presums[left-1] > newFlowers:
                break
            remains = newFlowers-(t*left-presums[left-1])
            right = max(right,left)
            while right < n and target*(n-right)-(presums[-1]-presums[right-1]) > remains:
                right += 1
            remains -= target*(n-right)-(presums[-1]-presums[right-1])
            # print(t,left,right,remains,t*partial+(m+n-right+remains//(target-t))*full)
            ans = max(ans,t*partial+(m+min(n-1,n-right+remains//(target-t)))*full)
        return ans


class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        flowers.sort()
        n = len(flowers)
        if flowers[0] >= target:  # 剪枝，此时所有花园都是完善的
            return n * full

        leftFlowers = newFlowers - target * n  # 填充后缀后，剩余可以种植的花
        for i in range(n):
            flowers[i] = min(flowers[i], target)
            leftFlowers += flowers[i]

        ans, x, sumFlowers = 0, 0, 0
        for i in range(n + 1):  # 枚举后缀长度 n-i
            if leftFlowers >= 0:
                # 计算最长前缀的长度
                while x < i and flowers[x] * x - sumFlowers <= leftFlowers:
                    sumFlowers += flowers[x]
                    x += 1  # 注意 x 只增不减，二重循环的时间复杂度为 O(n)
                beauty = (n - i) * full  # 计算总美丽值
                if x:
                    beauty += min((leftFlowers + sumFlowers) // x, target - 1) * partial
                ans = max(ans, beauty)
            if i < n:
                leftFlowers += target - flowers[i]
        return ans


作者：endlesscheng
链接：https://leetcode-cn.com/problems/maximum-total-beauty-of-the-gardens/solution/by-endlesscheng-10i7/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。




class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        flowers.sort()
        n, s, fcnt, j, T = len(flowers), sum(flowers), 0, len(flowers) - 1, target - 1
        
        res = 0
        
        while flowers and newFlowers >= 0:
            while j >= 0 and flowers[j] > T:
                s -= flowers[j]
                j -= 1
            
            if j >= 0:
                while T * (j + 1) - s > newFlowers:
                    T -= 1
                    while j >= 0 and flowers[j] > T:
                        s -= flowers[j]
                        j -= 1
                res = max(res, T * partial + (n - len(flowers)) * full)
            
            newFlowers -= max(0, target - flowers[-1])
            if j == len(flowers) - 1:
                s -= flowers[j]
                j -= 1
            flowers.pop()
        
        if newFlowers >= 0:
            res = max(res, n * full)
        
        return res


作者：newhar
链接：https://leetcode-cn.com/problems/maximum-total-beauty-of-the-gardens/solution/by-newhar-nk6l/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。