class Solution:
    def supersequences(self, words: List[str]) -> List[List[int]]:
        # 收集有哪些字母，同时建图
        all_mask = 0
        g = defaultdict(list)
        for x, y in words:
            x, y = ord(x) - ord('a'), ord(y) - ord('a')
            all_mask |= 1 << x | 1 << y
            g[x].append(y)

        # 判断是否有环
        def has_cycle(sub: int) -> bool:
            color = [0] * 26
            def dfs(x: int) -> bool:
                color[x] = 1
                for y in g[x]:
                    # 只遍历不在 sub 中的字母
                    if sub >> y & 1:
                        continue
                    if color[y] == 1 or color[y] == 0 and dfs(y):
                        return True
                color[x] = 2
                return False
            for i, c in enumerate(color):
                # 只遍历不在 sub 中的字母
                if c == 0 and (sub >> i & 1) == 0 and dfs(i):
                    return True
            return False

        st = set()
        min_size = inf
        # 枚举 all_mask 的所有子集 sub
        sub = all_mask
        while True:
            size = sub.bit_count()
            # 剪枝：如果 size > min_size 就不需要判断了
            if size <= min_size and not has_cycle(sub):
                if size < min_size:
                    min_size = size
                    st.clear()
                st.add(sub)
            sub = (sub - 1) & all_mask
            if sub == all_mask:
                break

        return [[(all_mask >> i & 1) + (sub >> i & 1) for i in range(26)]
                for sub in st]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/frequencies-of-shortest-supersequences/solutions/3057743/mei-ju-zi-ji-jian-tu-pan-duan-shi-fou-yo-n43u/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。