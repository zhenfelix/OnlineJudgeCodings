from typing import List

class Solution:
    def countEffective(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        # 1. 计算整个数组的按位或
        total_or = 0
        for x in nums:
            total_or |= x
            
        # 如果总 OR 为 0，说明所有元素都是 0，任何子序列移除后 OR 仍为 0，不严格递减
        if total_or == 0:
            return 0
        
        # 2. 准备 SOS DP
        # 最大值 10^6 < 2^20
        L = 20
        size = 1 << L
        dp = [0] * size
        
        # 统计频率
        for x in nums:
            dp[x] += 1
            
        # 执行 SOS DP (高维前缀和)
        # dp[mask] 将存储 nums 中是 mask 子掩码的元素个数
        for i in range(L):
            bit = 1 << i
            # 遍历所有掩码，如果当前位是 1，则累加对应位是 0 的状态
            for mask in range(0, size, 2 * bit):
                for k in range(mask, mask + bit):
                    dp[k + bit] += dp[k]
        
        # 预处理 2 的幂次
        n = len(nums)
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i-1] * 2) % MOD
            
        count_equal = 0
        
        # 3. 容斥原理计算 OR == total_or 的子集数量
        # 只需要遍历 total_or 的子掩码
        s = total_or
        while True:
            # dp[s] 是 nums 中属于 s 子掩码的元素个数
            # 这些元素组成的任意子集，其 OR 也是 s 的子掩码
            term = pow2[dp[s]]
            
            # 计算 (total_or - s) 的汉明重量（置位位数）的奇偶性
            # 用异或计算差异位
            diff = total_or ^ s
            # bit_count() 在 Python 3.10+ 可用
            if diff.bit_count() % 2 == 1:
                count_equal = (count_equal - term + MOD) % MOD
            else:
                count_equal = (count_equal + term) % MOD
                
            if s == 0:
                break
            #以此法高效遍历子掩码
            s = (s - 1) & total_or
            
        # 4. 结果为 总子集数 - OR等于TotalOR的子集数
        ans = (pow2[n] - count_equal + MOD) % MOD
        return ans