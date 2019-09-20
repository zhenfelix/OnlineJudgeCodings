# class Solution:
#     def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
#         cnt = 0
#         row, col = 0, 0
#         while True:
#             for word in sentence:
#                 if len(word) > cols:
#                     return 0
#                 if col >= cols:
#                     col, row = 0, row+1
#                 if col + len(word) <= cols:
#                     col = col+len(word)+1
#                     # if col >= cols:
#                     #     col, row = 0, row+1
#                 else:
#                     col, row = len(word)+1, row+1
                
#                 # print(row,col)
#             if row >= rows:
#                 return cnt   
#             cnt += 1

class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = ' '.join(sentence) + ' '
        n = len(s)
        count = 0

        for i in range(rows):
            count += cols
            if s[count % n] == ' ':
                count += 1
            else:
                while count > 0 and s[(count - 1) % n] != ' ':
                    count -= 1

        return count // n

