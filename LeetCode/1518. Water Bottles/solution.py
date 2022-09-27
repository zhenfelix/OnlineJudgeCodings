class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles - 1) // (numExchange - 1)


# 作者：si-gu-wo-huan-zai
# 链接：https://leetcode.cn/problems/water-bottles/solution/p-by-si-gu-wo-huan-zai-bwo5/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        p, q = numBottles//(numExchange-1), numBottles%(numExchange-1)
        return p*numExchange+q-(q==0)


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles:
            delta = numBottles//numExchange
            if delta == 0:
                break
            ans += delta
            numBottles = delta+(numBottles%numExchange)
        return ans 
