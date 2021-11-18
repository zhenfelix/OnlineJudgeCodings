class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        n = len(word)
        return sum(set(word[i:j+1]) == set(list('aeiou')) for i in range(n) for j in range(i,n))


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        n = len(word)
        candidates = set(list("aeiou"))
        pre = 0
        cc = Counter()
        cnt = 0
        res = 0
        left = 0
        for right, ch in enumerate(word):
            if ch not in candidates:
                pre = right+1
                left = right+1
                cc = Counter()
                cnt = 0
                continue
            if cc[ch] == 0:
                cnt += 1
            cc[ch] += 1
            while cnt == 5:
                cc[word[left]] -= 1
                if cc[word[left]] == 0:
                    cnt -= 1
                left += 1
            res += left-pre
        return res


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        n = len(word)
        next_consonant = [n] * n
        for i in range(n - 2, -1, -1):
            if word[i + 1] not in 'aeiou':
                next_consonant[i] = i + 1
            else:
                next_consonant[i] = next_consonant[i + 1]
        
        ans = 0
        l = 0
        r = -1
        cnt = collections.Counter()
        while l < n:
            r = max(r, l - 1)
            
            if word[l] not in 'aeiou':
                l += 1
                cnt = collections.Counter()
                continue
        
            jump = False
        
            while len(cnt) < 5 and r + 1 < n:
                r += 1
                if word[r] in 'aeiou':
                    cnt[word[r]] += 1
                else:
                    l = r + 1
                    jump = True
                    cnt = collections.Counter()
                    break
                    
            if jump:
                continue
                    
            if len(cnt) == 5:
                ans += next_consonant[r] - r
            
            if l < n:
                cnt[word[l]] -= 1
                if cnt[word[l]] == 0:
                    del cnt[word[l]]

            l += 1
        return ans


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/JXlHA8/view/dDXpJp/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。