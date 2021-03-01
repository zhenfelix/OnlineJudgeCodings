class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        res = []
        while word1 and word2:
            if word1 >= word2:
                res.append(word1[0])
                word1 = word1[1:]
            else:
                res.append(word2[0])
                word2 = word2[1:]
        res = ''.join(res)
        if word1:
            res = res + word1
        else:
            res = res + word2
        return res 