# class Solution:
#     def backspaceCompare(self, S: str, T: str) -> bool:
#         st1, st2 =[], []
#         for s in S:
#             if s=='#' and len(st1)>0:
#                 st1.pop()
#             elif s!='#':
#                 st1.append(s)
#         for t in T:
#             if t=='#' and len(st2)>0:
#                 st2.pop()
#             elif t!='#':
#                 st2.append(t)
#         return st1==st2

# class Solution:
#     def backspaceCompare(self, S: str, T: str) -> bool:
#         i, j = len(S)-1, len(T)-1
#         ci, cj = 0, 0
#         while i>=0 or j>=0:
#             while i>=0 and S[i]=='#':
#                 while i>=0 and S[i]=='#':
#                     ci+=1
#                     i-=1
#                 while i>=0 and ci>0 and S[i]!='#':
#                     ci-=1
#                     i-=1
#             while j>=0 and T[j]=='#':
#                 while j>=0 and T[j]=='#':
#                     cj+=1
#                     j-=1
#                 while j>=0 and cj>0 and T[j]!='#':
#                     cj-=1
#                     j-=1

#             if (i>=0 and j>=0 and S[i]!=T[j]) or (i<0 and j>=0) or (i>=0 and j<0):
                
#                 return False
#             i-=1
#             j-=1
#         return True


    # bool backspaceCompare(string S, string T) {
    #     for (int i = S.length() - 1, j = T.length() - 1;;i--, j--){
    #         for (int b = 0; i >= 0 && (b || S[i] == '#'); --i) b += S[i] == '#' ? 1 : -1;
    #         for (int b = 0; j >= 0 && (b || T[j] == '#'); --j) b += T[j] == '#' ? 1 : -1;
    #         if (i < 0 || j < 0 || S[i] != T[j]) return i == -1 && j == -1;
    #     }
    # }   
    
class Solution:
    def backspaceCompare(self, S, T):
        i, j = len(S) - 1, len(T) - 1
        backS = backT = 0
        while True:
            while i >= 0 and (backS or S[i] == '#'):
                backS += 1 if S[i] == '#' else -1
                i -= 1
            while j >= 0 and (backT or T[j] == '#'):
                backT += 1 if T[j] == '#' else -1
                j -= 1
            if not (i >= 0 and j >= 0 and S[i] == T[j]):
                return i == j == -1
            i, j = i - 1, j - 1