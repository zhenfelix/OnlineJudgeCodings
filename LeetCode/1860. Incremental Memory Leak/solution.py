class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        cnt = 1
        while memory1 or memory2:
            if memory1 < memory2:
                if cnt > memory2:
                    break
                memory2 -= cnt
            else:
                if cnt > memory1:
                    break
                memory1 -= cnt
            cnt += 1
            
        return [cnt, memory1, memory2]