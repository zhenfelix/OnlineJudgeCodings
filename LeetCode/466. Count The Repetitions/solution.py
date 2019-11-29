class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        i, j, cnt1 = 0, 0, 0
        arr = []
        mp = {0:0}
        loop = -1
        while cnt1 < n1:
            idx = j%len(s2)
            if s1[i] == s2[idx]:
                j += 1
                
            i += 1
            if i == len(s1):
                cnt1 += 1
                i = 0
                arr.append(j)
                if j%len(s2) in mp:
                    loop = mp[j%len(s2)]
                    break
                mp[j%len(s2)] = cnt1
        if loop == -1:
            return (j//len(s2))//n2
        # print(arr)
        # print(mp)
        # print(loop)
        prefix = arr[loop-1] if loop >= 1 else 0
        repeat = arr[-1]-prefix
        suffix = arr[(n1-loop)%(len(arr)-loop) - 1 + loop ] - prefix if (n1-loop)%(len(arr)-loop) > 0 else 0
        j = prefix + (n1-loop)//(len(arr)-loop)*repeat + suffix
        # print(prefix,repeat,suffix,j)
        return (j//len(s2))//n2


# - [C++ solution inspired by @70664914 with organized explanation](https://leetcode.com/problems/count-the-repetitions/discuss/95398/C++-solution-inspired-by-@70664914-with-organized-explanation)
#                     0 1    2 3 0      1    2 3 0      1    2 3 0  
# S1 --------------> abacb | abacb | abacb | abacb | abacb | abacb 

# repeatCount ----->    0  |   1   |   1   |   2   |   2   |   3

# Increment of 
# repeatCount     ->    0  |   1   |   0   |   1   |   0   |   1

# nextIndex ------->    2  |   1   |   2   |   1   |   2   |   1
#                                      ^
#                    |
#                    repetitive pattern found here (we've met 2 before)!
#                    The pattern repeated 3 times