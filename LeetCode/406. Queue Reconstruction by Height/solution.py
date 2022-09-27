class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        for h, c in sorted(people, key = lambda x: (-x[0],x[-1])):
            res.insert(c,[h,c])

        return res

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        for h, c in sorted(people, key = lambda x: (-x[0],x[-1])):
            # print(h,c,res)
            cnt = 0
            flag = True
            for i in range(len(res)):
                if cnt == c:
                    res.insert(i,[h,c])
                    flag = False
                    break
                if res[i][0] >= h:
                    cnt += 1
                
            if flag:
                res.append([h,c])

        return res