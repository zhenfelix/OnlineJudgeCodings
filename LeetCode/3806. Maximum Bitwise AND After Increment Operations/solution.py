from typing import List

class Solution:
    def maximumAND(self, nums: List[int], k: int, m: int) -> int:
        ans = 0
        # 从高位向低位贪心。10^9 < 2^30，所以从 30 开始足够覆盖所有情况。
        # 时间复杂度：30 * N * logN (主要是排序)
        for i in range(30, -1, -1):
            # 尝试将当前位 i 加入答案
            target = ans | (1 << i)
            costs = []
            
            for x in nums:
                # 1. 如果 x 已经包含 target 的所有位，代价为 0
                if (x & target) == target:
                    costs.append(0)
                    continue
                
                # 2. 找出 target 中有但 x 中没有的最高位 (MSB)
                # (target & ~x) 得到所有 x 缺失的位
                missing = target & ~x
                # bit_length() 返回二进制的长度，减 1 即为最高位下标
                msb = missing.bit_length() - 1
                
                # 3. 计算变成满足 target 的最小数值 next_val
                # 方法：
                # a. 保留 x 在 msb 之上的高位 (清空 msb 及以下)
                # b. 强制设置 msb 为 1
                # c. 强制设置 msb 以下的位为 target 需要的位
                
                # 清除 msb 及以下的位，只保留高位
                prefix = (x >> (msb + 1)) << (msb + 1)
                
                # 获取 target 在 msb 以下需要的位
                suffix = target & ((1 << msb) - 1)
                
                next_val = prefix | (1 << msb) | suffix
                
                costs.append(next_val - x)
            
            # 4. 检查最小的 m 个代价之和是否 <= k
            # 我们可以只取最小的 m 个进行求和
            # 如果 costs 数量不足 m 个（理论上不会，因为所有数都能被变成 target），
            # 这里的逻辑是通用的。
            
            # 优化：可以使用 nth_element 或 heap，但在 Python 中 sort 足够快
            costs.sort()
            
            # 如果前 m 个代价总和在 k 以内，说明该位可以置为 1
            if sum(costs[:m]) <= k:
                ans = target
                
        return ans