# import collections

# class Solution:
#     def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
#         res = []
#         n = len(phrases)
#         phrases = sorted(phrases)
#         mp = collections.defaultdict(list)
#         for i in range(n):
#             word = phrases[i].split(' ')[0]
#             mp[word].append(i)
#         # print(mp)
#         for i, phrase in enumerate(phrases):
#             word = phrase.split(' ')[-1]
#             for idx in mp[word]:
#                 # print(word, mp)
#                 if idx == i:
#                     continue
#                 if phrases[idx] != phrase:
#                     first = ' '.join(phrase.split(' ')[:-1])
#                     if len(first) > 0:
#                         first += ' '
#                     tmp = first + phrases[idx]
#                 else:
#                     tmp = phrase
#                 if len(res) == 0 or tmp != res[-1]:
#                     res.append(tmp)
            
#         # print(mp)
        
#         return res
            
    
class Solution(object):
    def beforeAndAfterPuzzles(self, phrases):
        ans = []
        for i, p1 in enumerate(phrases):
            a1 = p1.split()
            for j, p2 in enumerate(phrases):
                a2 = p2.split()
                if i!=j and a1[-1] == a2[0]:
                    ans.append(" ".join(a1 + a2[1:]))
        
        return sorted(set(ans))



class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        phrases = [p.split() for p in phrases]
        # print(phrases)
        n = len(phrases)
        res = []
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if phrases[i][-1] == phrases[j][0]:
                    res.append(' '.join(phrases[i]+phrases[j][1:]))
        return sorted(list(set(res)))