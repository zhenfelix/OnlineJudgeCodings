class Solution:
    def masterMind(self, solution: str, guess: str) -> List[int]:
        answer = [0,0]
        answer[0] = sum(x==y for x,y in zip(solution,guess))
        ccs, ccg = Counter(solution), Counter(guess)
        answer[1] = sum(min(ccs[ch],ccg[ch]) for ch in "RGBY")-answer[0]
        return answer