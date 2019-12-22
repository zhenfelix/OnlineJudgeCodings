# class Solution:
#     def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
#         res = []
#         st = []
#         cnt = 0
#         for i, word in enumerate(words):
#             if cnt+len(word) > maxWidth:
#                 cnt -= 1
#                 nums = len(st)-1
#                 spaces = maxWidth-cnt+nums
#                 tmp = ""
#                 # print(st,cnt,nums,spaces)
#                 for s in st:
#                     tmp += s
#                     if nums == 0:
#                         tmp += " "*spaces
#                         break
#                     if spaces%nums:
#                         space = spaces//nums + 1
#                     else:
#                         space = spaces//nums
#                     tmp += " "*space
#                     spaces -= space
#                     nums -= 1
#                 res.append(tmp)
#                 cnt = 0
#                 st = []
            
#             cnt += 1+len(word)
#             st.append(word)
#         if st:
#             tmp = " ".join(st)
#             tmp += " "*(maxWidth-len(tmp))
#             res.append(tmp)
#         return res

                
class Solution:
    def fullJustify(self, words, maxWidth):
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i%(len(cur)-1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]