# from functools import lru_cache
# class Solution:
#     @lru_cache(None)
#     def numberOfWays(self, num_people: int) -> int:
        
#         if num_people == 2:
#             return 1
#         res = 2*self.numberOfWays(num_people-2)
        
#         for i in range(2,num_people-3,2):
#             res += self.numberOfWays(i) * self.numberOfWays(num_people-2-i)
#         return res%(10**9 + 7)


class Solution:
    def numberOfWays(self, num_people: int) -> int:
        n=num_people//2
        from math import factorial
        return (factorial(2*n)//factorial(n)//factorial(n)//(n+1))%(10**9+7) 



作者：weak-chicken
链接：https://leetcode.cn/problems/handshakes-that-dont-cross/solution/zhi-jie-yong-qia-te-lan-shu-gong-shi-ke-yi-yi-xing/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



# the human-readable DP "one-line" python solution.
# Just think about the first people, 
# he's hand will split the others (exclude himself and his partner) into two groups (left, right).
# so the total number of handshakes will be the num of left group times the number of right group.
# and loop over all the possible splits.
# using lru_cache for speed up.

from functools import lru_cache
class Solution:
    @lru_cache(None)
    def numberOfWays(self, num_people: int) -> int:
        return sum(self.numberOfWays(n) * self.numberOfWays(num_people - 2 - n) \
                   for n in range(0, num_people, 2)) % 1000000007 if num_people > 2 else 1


MOD = 10**9+7
class Solution:
    @cache
    def numberOfWays(self, n: int) -> int:
        if n == 0:
            return 1
        ans = 0
        for i in range(0,n,2):
            ans += self.numberOfWays(i)*self.numberOfWays(n-2-i)
            ans %= MOD
        return ans
