# class Solution:
#     def arrangeWords(self, text: str) -> str:
#         arr = [(word,i) for i,word in enumerate(text.split(' '))]
#         first = arr[0][0]
#         first = first[0].lower()+first[1:]
#         arr[0] = (first,0)
#         arr.sort(key = lambda x: (len(x[0]),x[1]))
#         arr = [x[0] for x in arr]
#         first = arr[0]
#         first = first[0].upper()+first[1:]
#         arr[0] = first
#         return ' '.join(arr)

class Solution:
    def arrangeWords(self, text: str) -> str:
        return " ".join(sorted(text.split(" "), key=len)).capitalize()#stable sort