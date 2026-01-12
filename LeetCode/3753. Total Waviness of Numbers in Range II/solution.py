from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def count(s_num):
            n = len(s_num)
            
            # 使用 lru_cache 进行记忆化搜索
            # 状态：当前索引，是否受限，是否前导零，前一位数字，前前一位数字
            @lru_cache(None)
            def dfs(idx, tight, is_leading_zero, pre, ppre):
                # 递归终止条件：填完了所有位
                if idx == n:
                    return 1, 0  # 找到了 1 个有效数字，后续没有产生新的波动值
                
                limit = int(s_num[idx]) if tight else 9
                res_count = 0
                res_waviness = 0
                
                for d in range(limit + 1):
                    new_tight = tight and (d == limit)
                    new_leading_zero = is_leading_zero and (d == 0)
                    
                    if new_leading_zero:
                        # 依然是前导零，pre 和 ppre 保持无效状态 (-1)
                        c, w = dfs(idx + 1, new_tight, True, -1, -1)
                        res_count += c
                        res_waviness += w
                    else:
                        # 计算当前位填 d 后，上一位 pre 是否构成峰或谷
                        is_wave = 0
                        # 只有当 ppre 有效时（即已经有了 ppre 和 pre），才能判断 pre 是否为波峰波谷
                        if ppre != -1:
                            if pre > ppre and pre > d: # 峰
                                is_wave = 1
                            elif pre < ppre and pre < d: # 谷
                                is_wave = 1
                        
                        # 递归处理下一位
                        # 现在的 pre 变成下一层的 ppre，现在的 d 变成下一层的 pre
                        c, w = dfs(idx + 1, new_tight, False, d, pre)
                        
                        res_count += c
                        # 总波动值 = 后续产生的波动值 + (当前产生的贡献 * 后续方案数)
                        res_waviness += w + (c * is_wave)
            
            return res_count, res_waviness

            return dfs(0, True, True, -1, -1)[1]

        # 计算区间和：count(num2) - count(num1 - 1)
        return count(str(num2)) - count(str(num1 - 1))