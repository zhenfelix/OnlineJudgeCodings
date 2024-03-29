from typing import  List

class Node:
    def __init__(self):
        self.parent = None
        self.coin = 0
        self.coin_child = 0
        self.children = []
        self.cnt = 1


class Solution:
    def build(self, root):
        for child in root.children:
            self.build(child)
            root.cnt += child.cnt
        return

    def updateSingle(self, cur, val):
        if cur:
            cur.coin += val
            # cur.coin %= self.M
            self.updateSingle(cur.parent, val)
        return

    def updateSum(self, cur, val):
        sums = val * cur.cnt
        cur.coin += sums
        # cur.coin %= self.M
        cur.coin_child += val
        # cur.coin_child %= self.M
        self.updateSingle(cur.parent, sums)
        return

    def query(self, cur):
        res = cur.coin
        p = cur.parent
        # res %= self.M
        while p:
            res += p.coin_child*cur.cnt
            # res %= self.M
            p = p.parent
        return res

    def bonus(self, n: int, leadership: List[List[int]], operations: List[List[int]]) -> List[int]:
        mp = {}
        self.M = (10 ** 9) + 7
        for a, b in leadership:
            if a not in mp:
                mp[a] = Node()
            if b not in mp:
                mp[b] = Node()
            mp[a].children.append(mp[b])
            mp[b].parent = mp[a]

        self.build(mp[1])
        ans = []
        for op in operations:
            if op[0] == 1:
                self.updateSingle(mp[op[1]], op[2])
            elif op[0] == 2:
                self.updateSum(mp[op[1]], op[2])
            else:
                ans.append(self.query(mp[op[1]])%self.M)
        return ans

# class Solution:
#     def bonus(self, n: int, leadership: List[List[int]], operations: List[List[int]]) -> List[int]:
#
#         res = []
#         coin = [0] * (n + 1)
#         lead = {i: set() for i in range(1, n + 1)}
#         leader = [0] * (n + 1)
#         for l in leadership:
#             lead[l[0]].add(l[1])
#             leader[l[1]] = l[0]
#
#         def F1(i, c):
#             if i == 0: return
#             coin[i] += c
#             F1(leader[i], c)
#
#         def F2(i, c):
#             t = sum((F2(j, c) for j in lead[i]), 0) + c
#             coin[i] += t
#             return t
#
#         for ope in operations:
#             if ope[0] == 1:
#                 F1(ope[1], ope[2])
#
#             elif ope[0] == 2:
#                 t = F2(ope[1], ope[2])
#                 F1(leader[ope[1]], t)
#
#
#             else:
#                 res.append(coin[ope[1]])
#
#         return [r % 1000000007 for r in res]

#
# class Solution:
#     def bonus(self, n: int, leadership: List[List[int]], operations: List[List[int]]) -> List[int]:
#         mod = int(1e9 + 7)
#
#         class Node:
#             def __init__(self):
#                 self.p = -1
#                 self.c = []
#                 self.lazy = 0
#                 self.sum = 0
#                 self.size = 1
#
#         p = [Node() for i in range(n)]
#         for a, b in leadership:
#             a -= 1
#             b -= 1
#             p[b].p = a
#             p[a].c.append(b)
#
#         def dfs(r):
#             for c in p[r].c:
#                 p[r].size += dfs(c)
#             return p[r].size
#
#         for i in range(n):
#             if p[i].p == -1:
#                 dfs(i)
#
#         ans = []
#         for op in operations:
#             if len(op) == 3:
#                 o, n, l = op
#             else:
#                 o, n = op
#                 l = None
#             n -= 1
#             if o == 1:
#                 c = n
#                 while c != -1:
#                     p[c].sum += l
#                     c = p[c].p
#             elif o == 2:
#                 p[n].lazy += l
#                 c = n
#                 while c != -1:
#                     p[c].sum += l * p[n].size
#                     c = p[c].p
#             else:
#                 c = p[n].p
#                 anc = []
#                 while c != -1:
#                     anc.append(c)
#                     c = p[c].p
#                 for a in anc[::-1]:
#                     for c in p[a].c:
#                         p[c].lazy += p[a].lazy
#                         p[c].sum += p[a].lazy * p[c].size
#                     p[a].lazy = 0
#                 ans.append(p[n].sum % mod)
#         return ans

if __name__ == "__main__":
    sol = Solution()
    n = 451
    leadership = [[1, 145], [1, 359], [1, 199], [1, 383], [145, 353], [145, 32], [145, 376], [145, 165], [145, 18], [145, 352], [359, 89], [199, 402], [199, 163], [199, 105], [199, 294], [199, 316], [199, 186], [383, 79], [383, 183], [383, 42], [383, 147], [383, 108], [353, 408], [353, 277], [353, 323], [353, 174], [353, 54], [353, 387], [353, 220], [32, 8], [32, 193], [32, 286], [32, 169], [32, 131], [32, 233], [32, 410], [376, 244], [376, 389], [376, 369], [376, 269], [376, 162], [376, 451], [376, 260], [376, 69], [376, 90], [376, 273], [165, 170], [165, 395], [18, 297], [352, 115], [352, 30], [352, 374], [89, 23], [89, 254], [89, 180], [402, 227], [402, 336], [402, 399], [402, 371], [402, 407], [163, 243], [163, 392], [163, 444], [163, 298], [163, 45], [163, 59], [163, 156], [163, 272], [163, 417], [163, 215], [105, 51], [105, 439], [105, 46], [105, 231], [105, 119], [105, 128], [105, 134], [105, 264], [105, 83], [105, 203], [294, 442], [294, 48], [294, 221], [294, 276], [294, 222], [294, 17], [294, 268], [294, 446], [294, 382], [316, 255], [316, 224], [186, 50], [186, 349], [186, 416], [186, 87], [186, 267], [186, 217], [186, 113], [186, 167], [79, 13], [79, 251], [79, 152], [79, 340], [79, 19], [183, 423], [183, 101], [183, 127], [183, 38], [183, 393], [183, 175], [183, 35], [183, 304], [42, 26], [42, 313], [42, 40], [42, 275], [42, 263], [42, 354], [42, 149], [42, 307], [147, 168], [147, 351], [147, 245], [147, 262], [108, 429], [108, 329], [108, 344], [108, 413], [108, 356], [108, 92], [108, 327], [408, 447], [408, 314], [408, 325], [408, 20], [408, 406], [408, 34], [408, 414], [408, 120], [408, 326], [408, 367], [277, 2], [277, 172], [277, 330], [277, 302], [277, 139], [277, 443], [277, 67], [277, 148], [277, 97], [277, 248], [323, 44], [323, 194], [323, 214], [323, 39], [323, 159], [323, 106], [323, 198], [323, 280], [323, 52], [323, 258], [174, 60], [174, 378], [174, 242], [174, 78], [174, 164], [54, 138], [54, 404], [387, 208], [387, 347], [387, 397], [387, 14], [387, 320], [387, 25], [387, 94], [387, 210], [220, 261], [220, 122], [220, 95], [220, 74], [220, 16], [8, 401], [8, 305], [8, 270], [193, 141], [193, 370], [193, 361], [193, 202], [193, 28], [193, 343], [193, 438], [193, 11], [193, 226], [286, 22], [286, 205], [286, 166], [169, 6], [131, 36], [131, 129], [131, 391], [131, 341], [131, 236], [131, 73], [131, 235], [131, 419], [131, 61], [131, 27], [233, 153], [233, 77], [233, 287], [233, 315], [410, 415], [410, 209], [410, 213], [410, 396], [410, 33], [410, 56], [410, 434], [410, 179], [244, 99], [244, 151], [244, 358], [244, 300], [244, 84], [244, 66], [244, 360], [389, 333], [389, 291], [389, 112], [389, 130], [389, 31], [389, 88], [389, 372], [389, 394], [389, 317], [389, 289], [369, 21], [369, 58], [369, 445], [369, 428], [269, 420], [269, 182], [269, 335], [269, 150], [269, 322], [269, 427], [269, 303], [162, 185], [451, 184], [451, 318], [451, 433], [451, 436], [451, 348], [451, 100], [451, 123], [451, 285], [451, 421], [451, 350], [260, 437], [260, 342], [260, 424], [260, 311], [260, 171], [69, 450], [69, 400], [69, 126], [69, 403], [69, 309], [69, 321], [69, 362], [69, 266], [90, 247], [90, 239], [90, 190], [90, 299], [90, 121], [90, 181], [273, 47], [170, 282], [170, 338], [170, 386], [170, 24], [170, 357], [170, 405], [395, 70], [395, 422], [395, 114], [395, 96], [395, 293], [297, 103], [297, 229], [297, 71], [297, 188], [297, 98], [115, 332], [115, 146], [115, 390], [115, 157], [115, 10], [115, 425], [115, 398], [30, 207], [30, 91], [30, 312], [374, 271], [374, 189], [374, 449], [23, 388], [254, 68], [254, 196], [180, 173], [180, 230], [180, 278], [180, 191], [180, 346], [180, 324], [227, 37], [227, 219], [227, 107], [227, 306], [336, 448], [336, 296], [336, 197], [336, 249], [336, 284], [336, 363], [336, 111], [399, 53], [399, 15], [399, 256], [399, 81], [399, 142], [399, 228], [371, 253], [371, 211], [371, 319], [371, 3], [371, 411], [407, 118], [407, 206], [407, 82], [407, 328], [407, 64], [407, 80], [407, 75], [243, 178], [243, 93], [243, 29], [243, 364], [243, 223], [243, 365], [243, 216], [243, 225], [392, 137], [392, 373], [392, 110], [392, 250], [392, 234], [392, 195], [392, 381], [392, 7], [392, 43], [392, 57], [444, 212], [298, 192], [298, 432], [298, 232], [298, 143], [298, 76], [45, 426], [45, 283], [45, 281], [45, 124], [45, 140], [45, 384], [45, 257], [45, 201], [59, 144], [59, 339], [59, 117], [59, 345], [59, 86], [59, 5], [59, 418], [59, 292], [59, 379], [156, 187], [156, 161], [156, 337], [156, 104], [156, 334], [156, 385], [156, 41], [272, 290], [272, 116], [272, 246], [272, 288], [417, 12], [417, 237], [417, 431], [417, 160], [417, 308], [215, 295], [215, 375], [215, 4], [215, 409], [215, 380], [215, 136], [51, 49], [439, 259], [439, 9], [439, 377], [439, 135], [439, 252], [439, 440], [439, 176], [439, 435], [439, 177], [46, 301], [46, 441], [46, 72], [46, 355], [46, 65], [46, 412], [46, 274], [46, 218], [46, 158], [231, 368], [231, 241], [119, 240], [119, 204], [119, 331], [119, 155], [119, 200], [119, 125], [119, 154], [119, 55], [119, 63], [128, 62], [134, 279], [134, 310], [134, 265], [134, 132], [134, 102], [134, 366], [134, 430], [264, 109], [264, 133], [264, 238], [83, 85]]
    operations = [[3, 1], [3, 145], [3, 359], [1, 52, 49], [2, 262, 23], [3, 145], [2, 426, 1], [2, 152, 49], [2, 287, 16], [1, 182, 35], [3, 145], [1, 337, 37], [2, 151, 43], [2, 153, 39], [3, 359], [3, 359], [1, 313, 22], [1, 142, 23], [2, 435, 13], [1, 68, 18], [3, 1], [1, 62, 31], [1, 99, 44], [3, 145], [2, 18, 20], [2, 352, 4], [1, 210, 31], [1, 223, 16], [3, 359], [1, 29, 33], [1, 326, 28], [2, 447, 27], [3, 264], [1, 30, 38], [1, 179, 3], [2, 55, 3], [2, 371, 3], [2, 96, 39], [2, 97, 1], [3, 1], [2, 49, 35], [3, 145], [1, 64, 3], [1, 402, 50], [1, 371, 17], [3, 1], [2, 363, 30], [1, 35, 34], [2, 169, 37], [1, 115, 5], [2, 415, 31], [3, 145], [3, 145], [1, 103, 22], [1, 175, 35], [3, 359], [2, 303, 3], [1, 191, 17], [3, 1], [1, 304, 37], [1, 136, 10], [2, 334, 40], [2, 267, 19], [1, 429, 6], [1, 330, 36], [2, 164, 26], [3, 1], [3, 86], [1, 214, 12], [1, 54, 22], [3, 359], [3, 1], [1, 319, 38], [1, 74, 47], [3, 359], [2, 300, 22], [1, 421, 32], [1, 335, 3], [3, 1], [2, 234, 1], [2, 38, 19], [2, 406, 22], [2, 122, 21], [1, 315, 42], [3, 21], [3, 55], [3, 145], [3, 1], [3, 1], [2, 353, 41], [2, 325, 34], [1, 141, 41], [3, 145], [2, 228, 14], [3, 145], [1, 324, 23], [3, 145], [3, 418], [1, 263, 7], [3, 359], [1, 180, 36], [3, 359], [1, 301, 32], [1, 30, 10], [3, 145], [1, 264, 47], [2, 55, 18], [1, 60, 49], [3, 63], [3, 359], [2, 134, 29], [1, 331, 21], [2, 227, 22], [3, 359], [3, 145], [2, 289, 44], [1, 97, 21], [1, 71, 12], [3, 111], [1, 33, 6], [2, 11, 47], [3, 359], [1, 183, 28], [1, 62, 48], [1, 6, 7], [2, 319, 13], [3, 145], [2, 301, 39], [1, 189, 33], [3, 167], [2, 359, 6], [3, 359], [2, 274, 23], [3, 359], [2, 333, 26], [2, 209, 29], [1, 272, 40], [3, 1], [3, 1], [3, 359], [3, 145], [2, 60, 46], [3, 359], [2, 264, 9], [1, 411, 42], [1, 52, 6], [1, 378, 26], [1, 397, 23], [3, 145], [3, 353], [2, 52, 48], [1, 174, 21], [3, 359], [2, 55, 22], [2, 324, 37], [3, 359], [1, 36, 50], [3, 1], [2, 342, 1], [1, 295, 11], [1, 394, 13], [3, 1], [1, 81, 34], [3, 145], [2, 212, 20], [2, 425, 12], [3, 36], [1, 40, 26], [1, 295, 25], [2, 359, 10], [2, 194, 10], [3, 246], [1, 364, 14], [3, 1], [2, 416, 3], [1, 386, 31], [1, 351, 4], [3, 359], [1, 153, 33], [3, 145], [2, 249, 34], [2, 254, 7], [2, 44, 37], [3, 1], [2, 166, 9], [2, 214, 12], [1, 11, 21], [2, 264, 21], [2, 256, 18], [3, 359], [1, 28, 11], [2, 432, 2], [2, 441, 39], [1, 178, 15], [1, 438, 1], [1, 338, 19], [1, 23, 48], [2, 63, 25], [1, 439, 19], [1, 203, 35], [1, 311, 23], [2, 184, 7], [3, 1], [1, 289, 30], [1, 271, 41], [1, 254, 12], [2, 318, 31], [1, 91, 14], [3, 417], [2, 50, 40], [1, 384, 19], [1, 166, 47], [1, 96, 37], [2, 233, 15], [2, 60, 28], [1, 428, 48], [2, 361, 40], [3, 1], [1, 250, 29], [2, 206, 34], [2, 152, 37], [1, 297, 4], [3, 359], [3, 145], [1, 43, 29], [1, 114, 36], [2, 103, 2], [3, 359], [2, 316, 37], [1, 94, 15], [2, 420, 49], [3, 208], [3, 1], [1, 361, 45], [2, 339, 49], [1, 203, 33], [1, 138, 50], [2, 233, 38], [3, 1], [3, 359], [2, 131, 25], [2, 143, 16], [3, 311], [3, 145], [3, 427], [2, 34, 47], [3, 80], [3, 220], [3, 145], [3, 150], [3, 202], [1, 148, 2], [2, 396, 49], [1, 231, 18], [2, 399, 26], [1, 67, 46], [1, 77, 16], [1, 27, 2], [3, 145], [2, 7, 46], [1, 229, 22], [2, 278, 49], [2, 280, 26], [3, 359], [1, 245, 47], [3, 1], [3, 308], [2, 35, 26], [3, 1], [3, 1], [2, 68, 17], [2, 26, 48], [2, 364, 42], [3, 359], [1, 51, 48], [3, 145], [2, 341, 19], [1, 72, 3], [2, 378, 6], [3, 145], [3, 145], [1, 274, 11], [1, 384, 5], [3, 65], [1, 339, 36], [1, 320, 20], [2, 14, 29], [2, 140, 4], [2, 343, 19], [2, 226, 27], [2, 152, 23], [1, 141, 4], [2, 172, 44], [3, 145], [2, 390, 45], [2, 162, 30], [3, 145], [2, 134, 8], [2, 212, 29], [1, 63, 18], [2, 303, 37], [1, 80, 40], [2, 162, 6], [2, 160, 5], [3, 145], [3, 359], [1, 87, 35], [1, 233, 22], [2, 331, 44], [2, 223, 46], [1, 122, 5], [2, 399, 24], [2, 140, 9], [1, 366, 48], [1, 269, 25], [1, 362, 4], [2, 63, 9], [3, 211], [2, 435, 28], [3, 359], [3, 359], [2, 449, 14], [3, 145], [1, 319, 13], [3, 145], [2, 342, 24], [3, 108], [2, 328, 29], [1, 98, 11], [3, 384], [1, 42, 32], [2, 201, 49], [1, 184, 22], [2, 131, 9], [3, 120], [1, 193, 23], [2, 5, 17], [1, 216, 22], [2, 209, 6], [2, 156, 19], [2, 174, 9], [1, 247, 43], [1, 433, 15], [3, 309], [3, 359], [1, 195, 20], [2, 112, 5], [1, 209, 30], [3, 1], [1, 229, 5], [3, 1], [2, 62, 39], [2, 189, 8], [2, 230, 11], [2, 20, 2], [1, 416, 17], [2, 346, 7], [2, 346, 4], [2, 367, 46], [3, 215], [2, 434, 31], [2, 216, 19], [3, 359], [1, 295, 17], [2, 253, 15], [1, 164, 15], [1, 359, 22], [1, 71, 27], [1, 276, 6], [3, 1], [1, 106, 15], [2, 380, 34], [3, 145], [3, 448], [3, 359], [1, 403, 7], [3, 145], [2, 290, 14], [1, 143, 14], [2, 300, 29], [2, 5, 6], [3, 359], [2, 175, 38], [1, 13, 45], [2, 430, 2], [1, 334, 41], [2, 103, 11], [3, 50], [1, 53, 42], [2, 165, 12], [2, 348, 5], [3, 145], [3, 359], [2, 45, 35], [2, 220, 18], [3, 372], [3, 1], [3, 145], [1, 54, 19], [3, 359], [3, 359], [1, 207, 19], [3, 1], [3, 359], [2, 43, 37], [2, 207, 9], [1, 251, 7], [2, 445, 48], [3, 244], [1, 448, 32], [1, 298, 32], [1, 267, 37], [3, 145], [2, 9, 24], [1, 189, 14], [3, 145], [1, 152, 31], [2, 328, 38], [1, 435, 30], [2, 427, 17], [3, 359], [1, 309, 47], [2, 103, 6], [1, 435, 39], [1, 313, 9], [1, 233, 38], [3, 145], [3, 359], [3, 359], [2, 260, 15], [1, 318, 38], [1, 122, 12], [3, 359], [1, 34, 19], [2, 81, 20], [1, 387, 14], [1, 240, 33], [2, 305, 19], [2, 316, 49], [3, 1], [1, 348, 24], [2, 311, 13], [2, 346, 29], [3, 145], [3, 145], [2, 71, 20], [2, 146, 32], [1, 187, 44], [3, 1], [1, 3, 3], [3, 359], [3, 359], [2, 344, 2], [2, 403, 1], [2, 194, 31], [3, 1], [2, 435, 19], [2, 220, 32], [1, 113, 5], [1, 165, 19], [1, 435, 19], [2, 111, 40], [1, 301, 41], [3, 359], [2, 72, 28], [2, 416, 46], [1, 60, 28], [3, 359], [3, 1], [2, 225, 4], [2, 122, 44], [1, 1, 27], [3, 359], [2, 69, 5], [3, 359], [2, 148, 25], [1, 27, 27], [3, 145], [2, 214, 31], [2, 375, 11], [2, 449, 22], [2, 286, 1], [3, 145], [2, 197, 44], [1, 315, 41], [2, 289, 38], [1, 308, 13], [1, 383, 9], [3, 167], [3, 359], [3, 1], [2, 30, 5], [2, 61, 45], [1, 232, 28], [3, 145], [1, 221, 43], [2, 433, 17], [1, 52, 38], [2, 109, 1], [2, 238, 3]]

    print(sol.bonus(n,leadership,operations))