class Solution:
    def printVertically(self, s):
        columns = s.split()
        rows = itertools.zip_longest(*columns, fillvalue=' ')
        print(list(rows))
        return [''.join(row).rstrip() for row in rows]


class Solution:
    def printVertically(self, s: str) -> List[str]:
        mat = s.split(' ')
        n = max(map(len,mat))
        # print(n,mat)
        res = []
        for i in range(n):
            tmp = ""
            for j in range(len(mat)):
                if i < len(mat[j]):
                    tmp += mat[j][i]
                else:
                    tmp += " "
            k = len(mat)-1
            while tmp[k] == " ":
                k -= 1
            res.append(tmp[:k+1])
        return res