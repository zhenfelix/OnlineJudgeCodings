import bisect

class Solution:
    def minOperations(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        n = len(nums)
        
        # --- 1. 可行性预处理 (Feasibility Check) ---
        # bad[i] 表示 nums[i] 和 nums[i-1] 是否模 k 不同
        # 如果 bad_pref[r+1] - bad_pref[l+1] > 0，说明区间 [l, r] 内有不同的模数
        bad = [0] * n
        for i in range(1, n):
            if nums[i] % k != nums[i-1] % k:
                bad[i] = 1
        
        bad_pref = [0] * (n + 1)
        for i in range(n):
            bad_pref[i+1] = bad_pref[i] + bad[i]

        # --- 2. 离散化 (Discretization) ---
        # 主席树是基于值域的，因为值很大，所以需要离散化
        sorted_unique = sorted(list(set(nums)))
        val_map = {val: i for i, val in enumerate(sorted_unique)}
        m = len(sorted_unique)
        
        # --- 3. 主席树构建 (Persistent Segment Tree) ---
        # 由于 Python 对象开销大，使用数组模拟静态链表
        # 空间估算：每次更新增加 logM 个节点。N=40000, M<=40000. 
        # 节点数大约 N * 20。预留足够空间。
        MAX_NODES = n * 20 + m * 4 + 100
        
        l_child = [0] * MAX_NODES
        r_child = [0] * MAX_NODES
        tree_cnt = [0] * MAX_NODES  # 区间内数字个数
        tree_sum = [0] * MAX_NODES  # 区间内数字之和
        roots = [0] * (n + 1)       # 存储每个版本的根节点
        
        node_ptr = 1 # 0 号节点作为空节点/null
        
        def build(l, r):
            nonlocal node_ptr
            idx = node_ptr
            node_ptr += 1
            if l == r:
                return idx
            mid = (l + r) // 2
            l_child[idx] = build(l, mid)
            r_child[idx] = build(mid + 1, r)
            return idx

        # 初始化空树（版本 0）
        roots[0] = build(0, m - 1)

        def update(prev_node, l, r, target_val_idx, real_val):
            nonlocal node_ptr
            idx = node_ptr
            node_ptr += 1
            
            # 复制前一个版本的信息
            l_child[idx] = l_child[prev_node]
            r_child[idx] = r_child[prev_node]
            tree_cnt[idx] = tree_cnt[prev_node] + 1
            tree_sum[idx] = tree_sum[prev_node] + real_val
            
            if l == r:
                return idx
            
            mid = (l + r) // 2
            if target_val_idx <= mid:
                l_child[idx] = update(l_child[prev_node], l, mid, target_val_idx, real_val)
            else:
                r_child[idx] = update(r_child[prev_node], mid + 1, r, target_val_idx, real_val)
            return idx

        # 生成所有版本
        for i, val in enumerate(nums):
            roots[i+1] = update(roots[i], 0, m - 1, val_map[val], val)

        # --- 4. 查询函数 ---
        
        # 寻找区间 [q_l, q_r] 内第 k 小的值 (返回的是离散化后的索引)
        # 通过将两个版本的线段树节点相减 (root_r - root_l) 来获取区间信息
        def query_kth(node_u, node_v, l, r, k):
            if l == r:
                return l
            mid = (l + r) // 2
            # 左子树包含的数字个数
            left_count = tree_cnt[l_child[node_v]] - tree_cnt[l_child[node_u]]
            
            if k <= left_count:
                return query_kth(l_child[node_u], l_child[node_v], l, mid, k)
            else:
                return query_kth(r_child[node_u], r_child[node_v], mid + 1, r, k - left_count)

        # 查询区间 [q_l, q_r] 内，排名 <= limit_idx 的所有数的 (个数, 和)
        def query_stats(node_u, node_v, l, r, limit_idx):
            if l == r:
                # 到了叶子节点，返回该节点的个数与和
                c = tree_cnt[node_v] - tree_cnt[node_u]
                s = tree_sum[node_v] - tree_sum[node_u]
                return c, s
            
            mid = (l + r) // 2
            if limit_idx <= mid:
                # 限制在左边，只需要查左子树
                return query_stats(l_child[node_u], l_child[node_v], l, mid, limit_idx)
            else:
                # 限制在右边，左子树全要，右子树递归查
                c_left = tree_cnt[l_child[node_v]] - tree_cnt[l_child[node_u]]
                s_left = tree_sum[l_child[node_v]] - tree_sum[l_child[node_u]]
                c_right, s_right = query_stats(r_child[node_u], r_child[node_v], mid + 1, r, limit_idx)
                return c_left + c_right, s_left + s_right

        ans = []
        for l, r in queries:
            # 1. 检查是否可行
            if bad_pref[r+1] - bad_pref[l+1] > 0:
                ans.append(-1)
                continue
            
            if l == r:
                ans.append(0)
                continue

            # 2. 找到中位数
            total_len = r - l + 1
            median_rank = (total_len + 1) // 2
            
            # 使用 root[r+1] 和 root[l] 代表区间 [l, r]
            root_u = roots[l]
            root_v = roots[r+1]
            
            median_idx = query_kth(root_u, root_v, 0, m - 1, median_rank)
            median_val = sorted_unique[median_idx]
            
            # 3. 计算代价
            # 获取小于等于中位数的元素的 个数 和 总和
            cnt_left, sum_left = query_stats(root_u, root_v, 0, m - 1, median_idx)
            
            # 获取区间所有元素的 个数 和 总和
            total_cnt = tree_cnt[root_v] - tree_cnt[root_u] # 实际上就是 total_len
            total_sum = tree_sum[root_v] - tree_sum[root_u]
            
            cnt_right = total_cnt - cnt_left
            sum_right = total_sum - sum_left
            
            # 代价 = (左边变成中位数的代价) + (右边变成中位数的代价)
            # 左边代价 = cnt_left * median - sum_left
            # 右边代价 = sum_right - cnt_right * median
            cost = (cnt_left * median_val - sum_left) + (sum_right - cnt_right * median_val)
            
            ans.append(cost // k)
            
        return ans