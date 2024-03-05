class KMP:
    def partial(self, pattern):
        """ Calculate partial match table: String -> [Int]"""
        ret = [0]
        
        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret
        
    def search(self, T, P):
        """ 
        KMP search main algorithm: String -> String -> [Int] 
        Return all the matching position of pattern string P in T
        """
        partial, ret, j = self.partial(P), [], 0
        
        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j - 1]
            if T[i] == P[j]: j += 1
            if j == len(P): 
                ret.append(i - (j - 1))
                j = partial[j - 1]
            
        return ret

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        for i in range(n-1):
            if nums[i+1] > nums[i]:
                nums[i] = 1
            elif nums[i+1] == nums[i]:
                nums[i] = 0
            else:
                nums[i] = -1
        kmp = KMP()
        ans = kmp.search(nums,pattern)
        return len(ans)




class KMP:
    def partial(self, pattern):
        m = len(pattern)
        match = [-1]*m 
        for i in range(1,m):
            j = match[i-1]
            while j != -1 and pattern[i] != pattern[j+1]:
                j = match[j]
            if pattern[i] == pattern[j+1]:
                match[i] = j+1
        return match

    def search(self, pattern, s):
        match = self.partial(pattern)
        n = len(s)
        m = len(match)
        ans = []
        j = -1
        for i in range(n):
            while j != -1 and pattern[j+1] != s[i]:
                j = match[j]
            if s[i] == pattern[j+1]:
                j += 1
            if j == m-1:
                ans.append(i-m+1)
                j = match[j]
        return ans 
        
class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        for i in range(n-1):
            if nums[i+1] > nums[i]:
                nums[i] = 1
            elif nums[i+1] == nums[i]:
                nums[i] = 0
            else:
                nums[i] = -1
        kmp = KMP()
        ans = kmp.search(pattern,nums)
        return len(ans)

