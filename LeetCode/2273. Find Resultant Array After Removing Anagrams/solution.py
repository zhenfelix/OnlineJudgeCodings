class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = [words[0]]
        n = len(words)
        for i in range(1,n):
            pre = Counter(ans[-1])
            cur = Counter(words[i])
            if cur != pre:
                ans.append(words[i])
        return ans