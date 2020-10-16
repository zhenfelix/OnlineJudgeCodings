class Solution:
    def bestRotation(self, A: List[int]) -> int:
        cc = defaultdict(int)
        idx, res, cur, level, n = 0, 0, 0, 0, len(A)
        for i, a in enumerate(A):
            A[i] = a - i
            cc[A[i]] += 1
        for i, a in enumerate(A):
            cc[a] -= 1
            if a <= level:
                cur -= 1
            cc[a-n] += 1
            if a - n <= level:
                cur += 1
            cur -= cc[level]
            level -= 1
            if cur > res:
                idx, res = i+1, cur
        return idx


    # def bestRotation(self, A):
    #     N = len(A)
    #     change = [1] * N
    #     for i in range(N): change[(i - A[i] + 1) % N] -= 1
    #     for i in range(1, N): change[i] += change[i - 1]
    #     return change.index(max(change))
