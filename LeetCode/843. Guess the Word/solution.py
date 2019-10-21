# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

# class Solution(object):
#     def findSecretWord(self, wordlist, master):
#         n = 0
#         while n < 6:
#             guess = random.choice(wordlist)
#             n = master.guess(guess)
#             wordlist = [w for w in wordlist if sum(i == j for i, j in zip(guess, w)) == n]     

#     def match(self, a, b):
#         return sum([i==j for i,j in zip(a,b)])
    
#     def findSecretWord(self, wordlist, master):
#         n = 0
#         while n < 6:
#             count = collections.Counter(w1 for w1, w2 in itertools.permutations(wordlist, 2) if self.match(w1, w2) == 0)
#             guess = min(wordlist, key=lambda w: count[w])
#             n = master.guess(guess)
#             wordlist = [w for w in wordlist if self.match(w, guess) == n]

from collections import defaultdict
class Solution(object):
    def findSecretWord(self, wordlist, master):
        def worstCnt(guess, candidates):
            res = 0
            cnt = defaultdict(int)
            for candidate in candidates:
                cc = sum([i==j for i,j in zip(guess,candidate)])
                cnt[cc] += 1
                res = max(res,cnt[cc])
            return res

        def selectBestGuess(guesses, candidates):
            return min(guesses, key = lambda x: worstCnt(x, candidates))

        matches = 0
        guess_words, target_candidates = [w for w in wordlist], [w for w in wordlist]
        # while matches < 6:
        #     guess_word = selectBestGuess(target_candidates, target_candidates)
        #     matches = master.guess(guess_word)
        #     target_candidates = [w for w in target_candidates if sum(i == j for i, j in zip(guess_word, w)) == matches]
            # print(guess_word)
            # print(matches)
            # print(target_candidates)
        while len(target_candidates) > 1:
            guess_word = selectBestGuess(guess_words, target_candidates)
            matches = master.guess(guess_word)
            target_candidates = [w for w in target_candidates if sum(i == j for i, j in zip(guess_word, w)) == matches]
        if target_candidates:
            master.guess(target_candidates[0])