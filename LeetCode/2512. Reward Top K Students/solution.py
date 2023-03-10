class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)
        def func(sent):
            s = 0
            for word in sent.split():
                if word in positive_feedback:
                    s += 3
                if word in negative_feedback:
                    s -= 1
            # print(sent,s)
            return s 
        score = list(map(func,report))
        ans = [(-s,sid) for s,sid in zip(score,student_id)]
        ans.sort()
        # print(ans)
        return [sid for _, sid in ans[:k]]