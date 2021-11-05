class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        ops = []
        digits = []
        for ch in s:
            if ch in ['+','*']:
                ops.append(ch)
            else:
                digits.append(ord(ch)-ord('0'))
        n = len(ops)

        @lru_cache(None)
        def dfs(i,j):
            if i == j:
                return set([digits[i]])
            res = set()
            for k in range(i,j):
                left = dfs(i,k)
                right = dfs(k+1,j)
                for l in left:
                    for r in right:
                        v = l+r if ops[k] == '+' else l*r
                        if v <= 1000:
                            res.add(v)
            return res
            
        
        def calc():
            tmp = [digits[0]]
            for i in range(n):
                if ops[i] == '*':
                    tmp[-1] *= digits[i+1]
                else:
                    tmp.append(digits[i+1])
            return sum(tmp)

        mistakes = dfs(0,n)
        correct = calc()

        ans = 0
        for a in answers:
            if a == correct:
                ans += 5
            elif a in mistakes:
                ans += 2
        return ans


