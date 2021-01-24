# class Solution:
#     def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
#         m = len(languages)
#         res = m
#         for i in range(1,n+1):
#             cnt, seen = 0, defaultdict(set)
#             for j, language in enumerate(languages):
#                 seen[j+1] = set(language)
#             for a, b in friendships:
#                 if seen[a]&seen[b]:
#                     continue
#                 if i not in seen[a]:
#                     cnt += 1
#                     seen[a].add(i)
#                 if i not in seen[b]:
#                     cnt += 1
#                     seen[b].add(i)
#             res = min(res, cnt)
#         return res 

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        m = len(languages)
        res, cc, seen = m, defaultdict(set), defaultdict(set)
        for j, language in enumerate(languages):
            seen[j+1] = set(language)
        for a, b in friendships:
            if seen[a]&seen[b]:
                continue
            for i in range(1,n+1):
                if i not in seen[a]:
                    cc[i].add(a)
                if i not in seen[b]:
                    cc[i].add(b)
        for i in range(1,n+1):
            res = min(res, len(cc[i]))
        return res 


    # def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
    #     languages = [set(l) for l in languages]

    #     dontspeak = set()
    #     for u, v in friendships:
    #         u = u-1
    #         v = v-1
    #         if languages[u] & languages[v]: continue
    #         dontspeak.add(u)
    #         dontspeak.add(v)

    #     langcount = Counter()
    #     for f in dontspeak:
    #         for l in languages[f]:
    #             langcount[l] += 1

    #     return 0 if not dontspeak else len(dontspeak) - max(list(langcount.values()))