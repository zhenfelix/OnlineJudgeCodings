class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        state = defaultdict(int)
        for row, col in reservedSeats:
            if col in [1,10]:
                continue
            if col <= 5:
                state[row] |= (1<<2)
            if col >= 6:
                state[row] |= (1<<0)
            if 4 <= col <= 7:
                state[row] |= (1<<1)
        sums = 0
        for row, s in state.items():
            if s == 7:
                sums += 2
            else:
                sums += 1
        return n*2-sums