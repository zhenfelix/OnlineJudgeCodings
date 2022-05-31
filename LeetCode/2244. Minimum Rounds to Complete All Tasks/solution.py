class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cc = Counter(tasks)
        cnt = 0
        for k, v in cc.items():
            if v == 1:
                return -1
            elif v%3 == 1:
                cnt += (v-4)//3+2
            elif v%3 == 2:
                cnt += (v-2)//3+1
            else:
                cnt += v//3
        return cnt

