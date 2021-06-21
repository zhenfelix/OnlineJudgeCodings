class Solution:
    def halfQuestions(self, questions: List[int]) -> int:
        n = len(questions)//2
        cc = Counter(questions)
        cnt = 0
        for i in sorted([v for k, v in cc.items()], reverse = True):
            n -= i 
            cnt += 1
            if n <= 0:
                break
        return cnt 