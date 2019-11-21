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