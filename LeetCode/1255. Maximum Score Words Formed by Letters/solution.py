# from collections import Counter
# class Solution:
#     def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
#         def dfs(idx, cc):
#             if idx == -1:
#                 return 0
#             res = dfs(idx-1, cc.copy())
#             word_cc = Counter(words[idx])
#             word_score = 0
#             for k, v in word_cc.items():
#                 cc[k] -= v
#                 word_score += score[ord(k)-ord('a')]*v
#                 if cc[k] < 0:
#                     return res
#             res = max(res, word_score+dfs(idx-1, cc.copy()))
#             return res

#         letter_cc = Counter(letters)
#         return dfs(len(words)-1, letter_cc.copy())


class Solution():
    def maxScoreWords(self, words, letters, score):
        self.max_score = 0
        words_score = [sum(score[ord(c)-ord('a')] for c in word) for word in words]
        words_counter = [collections.Counter(word) for word in words]
        
        def dfs(i, curr_score, counter):
            if curr_score + sum(words_score[i:]) <= self.max_score:
                return
            self.max_score = max(self.max_score, curr_score)
            for j, wcnt in enumerate(words_counter[i:], i):
                if all(n <= counter.get(c,0) for c,n in wcnt.items()):
                    dfs(j+1, curr_score+words_score[j], {c:n-wcnt.get(c,0) for c,n in counter.items()})
        
        dfs(0, 0, collections.Counter(letters))
        return self.max_score