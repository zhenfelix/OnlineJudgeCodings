# class Solution:
#     def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
#         graph=collections.defaultdict(dict)
#         bfs=collections.deque()
#         ans=set()
#         bfs.append(text)
#         for k,v in synonyms:
#             graph[k][v]=1
#             graph[v][k]=1
#         while bfs:
#             curT=bfs.popleft()
#             ans.add(curT)
#             words=curT.split()
#             for i,w in enumerate(words):
#                 if w in graph.keys():
#                     for newW in graph[w]:
#                         newsent=' '.join(words[:i]+[newW]+words[i+1:])
#                         if newsent not in ans:
#                             bfs.append(newsent)
#         return sorted(list(ans))


class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        mp = {}
        sorted_syn = []
        for i, synonym in enumerate(synonyms):
            if synonym[0] in mp or synonym[1] in mp:
                if synonym[0] in mp:
                    sorted_syn[mp[synonym[0]]].append(synonym[1])
                else:
                    sorted_syn[mp[synonym[1]]].append(synonym[0])
            else:
                mp[synonym[0]] = mp[synonym[1]] = len(sorted_syn)
                sorted_syn.append([synonym[0],synonym[1]])
        
            
        for i, syn in enumerate(sorted_syn):
            sorted_syn[i] = sorted(syn)
            
        # print(sorted_syn)

        def dfs(path):
            idx = len(path)
            if idx == n:
                res.append(' '.join(path))
                return

            if text[idx] in mp:
                for synonym in sorted_syn[mp[text[idx]]]:
                    dfs(path+[synonym])

            else:
                dfs(path+[text[idx]])
            return

        text = text.split(" ")
        n = len(text)
        res = []
        dfs([])
        return res

    