class Solution(object):
    
    def countSubstrings(self, S):
        def manachers(S):
            A = '#'+'#'.join(S)+'#'
            Z = [0] * len(A)
            center = reach = 0
            for i in range(len(A)):
                if i < reach:
                    Z[i] = min(reach - i, Z[2 * center - i])
                while i - Z[i] - 1 >= 0 and i + Z[i] + 1 < len(A) and A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                    Z[i] += 1
                if i + Z[i] > reach:
                    center, reach = i, i + Z[i]
            return Z
        return sum((v+1)//2 for v in manachers(S))
        
