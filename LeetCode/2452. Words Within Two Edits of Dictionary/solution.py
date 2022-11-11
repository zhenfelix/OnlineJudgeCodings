class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def check(a,b):
            cnt = 0
            for aa,bb in zip(a,b):
                if aa != bb:
                    cnt += 1
            return cnt <= 2
        ans = []
        for word in queries:
            for can in dictionary:
                if check(word,can):
                    ans.append(word)
                    break
        return ans 