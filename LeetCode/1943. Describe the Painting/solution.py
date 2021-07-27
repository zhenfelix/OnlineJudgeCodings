class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        # segments.sort(key=lambda x: (x[-1], x[0], x[1]))
        # color = -1
        # arr = []
        # for s, e, c in segments:
        #     if c == color and arr and arr[-1][-2] >= s:
        #         arr[-1][2] = max(arr[-1][-2], e)
        #     else:
        #         arr.append([s,e,c])
        #     color = c 
        points = []
        for s, e, c in segments:
            points.append((s,c))
            points.append((e,-c))
        points.sort()
        color = 0
        pre = 0
        res = []
        for cur, c in points:
            if color > 0 and cur > pre:
                res.append([pre,cur,color])
            color += c 
            pre = cur
        return res