class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        s = "aeiou"
        nums = []
        for w in words:
            if w[0] in s and w[-1] in s:
                nums.append(1)
            else:
                nums.append(0)
        sums = [0]
        for x in nums:
            sums.append(sums[-1]+x)
        ans = []
        for l, r in queries:
            ans.append(sums[r+1]-sums[l])
        return ans 