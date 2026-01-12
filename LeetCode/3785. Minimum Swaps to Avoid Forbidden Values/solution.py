import collections
from typing import List

class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
        # 1. 数据统计
        # c_nums: 统计 nums 中每个数字的实际持有量（总供给）
        # c_forbid: 统计 forbidden 中每个数字被禁止的位置数量
        c_nums = collections.Counter(nums)
        c_forbid = collections.Counter(forbidden)
        n = len(nums)
        
        # 2. 可行性检查 (基于抽屉原理/霍尔定理)
        # 核心逻辑：对于任意数值 v，允许放 v 的坑位必须足够容纳所有的 v。
        # 允许的位置数 = 总长度 n - 禁止 v 的位置数 c_forbid[v]
        # 必须满足：c_nums[v] <= n - c_forbid[v]
        # 移项得：c_nums[v] + c_forbid[v] <= n
        for val, count in c_nums.items():
            if count + c_forbid[val] > n:
                return -1
        
        # 3. 识别冲突
        # 找出所有 nums[i] == forbidden[i] 的坏值
        bad_vals = [x for x, f in zip(nums, forbidden) if x == f]
        total_bad = len(bad_vals)
        
        # 如果没有冲突，无需任何操作
        if total_bad == 0:
            return 0
            
        # 4. 计算核心指标
        # max_freq: 冲突最严重的那个数值出现的次数（众数）
        # 这是衡量冲突分布是否均匀的关键
        max_freq = max(collections.Counter(bad_vals).values())
        
        # 5. 返回结果 (基于贪心构造)
        # 答案取决于以下两个下限的最大值：
        #
        # 下限 A: (total_bad + 1) // 2
        #   - 对应策略：内部置换 (Local Swap)
        #   - 逻辑：理想情况下，每次交换两个“不同数值”的坏值，一次操作解决 2 个冲突。
        #   - 公式等价于 ceil(total_bad / 2)。
        #   - 适用：当冲突分布均匀时，这决定了最小步数。
        #
        # 下限 B: max_freq
        #   - 对应策略：全局置换 (Global Swap)
        #   - 逻辑：如果某个坏值 X 太多 (max_freq > total_bad / 2)，它无法完全在内部配对。
        #     剩余的 X 必须去“非冲突区域”找好位置交换（1换1）。
        #     这意味着处理这 max_freq 个 X 至少需要 max_freq 次操作。
        #   - 适用：当冲突严重偏科时，众数数量成为硬瓶颈。
        
        return max((total_bad + 1) // 2, max_freq)