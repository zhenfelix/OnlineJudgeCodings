class Solution:
    def calc_pi(self, pattern: str) -> List[int]:
        pi = [0] * len(pattern)
        cnt = 0
        for i in range(1, len(pi)):
            b = pattern[i]
            while cnt > 0 and pattern[cnt] != b:
                cnt = pi[cnt - 1]
            if pattern[cnt] == b:
                cnt += 1
            pi[i] = cnt
        return pi

    def kmp_search(self, text: List[str], pattern: str, pi: List[int]) -> List[int]:
        n, k = len(text), len(pattern)
        diff = [0] * (n + 1)
        cnt = 0
        for i, b in enumerate(text):
            while cnt > 0 and pattern[cnt] != b:
                cnt = pi[cnt - 1]
            if pattern[cnt] == b:
                cnt += 1
            if cnt == k:
                diff[i - k + 1] += 1
                diff[i + 1] -= 1
                cnt = pi[cnt - 1]
        return list(accumulate(diff[:n]))

    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        h_text = [c for row in grid for c in row]
        v_text = [c for col in zip(*grid) for c in col]

        pi = self.calc_pi(pattern)
        in_pattern_h = self.kmp_search(h_text, pattern, pi)
        in_pattern_v = self.kmp_search(v_text, pattern, pi)

        m, n = len(grid), len(grid[0])
        ans = 0
        for i, in_h in enumerate(in_pattern_h):
            if in_h and in_pattern_v[i % n * m + i // n]:
                ans += 1
        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/solutions/3663069/kmp-chai-fen-shu-zu-pythonjavacgo-by-end-h5mz/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。