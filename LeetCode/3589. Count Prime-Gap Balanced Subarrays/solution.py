MX = 50_001
is_prime = [False] * 2 + [True] * (MX - 2)
for i in range(2, isqrt(MX) + 1):
    if is_prime[i]:
        for j in range(i * i, MX, i):
            is_prime[j] = False  # j 是质数 i 的倍数

class Solution:
    def primeSubarray(self, nums: List[int], k: int) -> int:
        min_q = deque()
        max_q = deque()
        last = last2 = -1
        ans = left = 0

        for i, x in enumerate(nums):
            if is_prime[x]:
                # 1. 入
                last2 = last
                last = i

                while min_q and x <= nums[min_q[-1]]:
                    min_q.pop()
                min_q.append(i)

                while max_q and x >= nums[max_q[-1]]:
                    max_q.pop()
                max_q.append(i)

                # 2. 出
                while nums[max_q[0]] - nums[min_q[0]] > k:
                    left += 1
                    if min_q[0] < left:
                        min_q.popleft()
                    if max_q[0] < left:
                        max_q.popleft()

            # 3. 更新答案
            ans += last2 - left + 1

        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/count-prime-gap-balanced-subarrays/solutions/3705577/yu-chu-li-zhi-shu-hua-dong-chuang-kou-da-v23w/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。