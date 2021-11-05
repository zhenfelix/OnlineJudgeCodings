维护动态区间的最小值
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        mp = {ch:i for i, ch in enumerate(s)}
        q = []
        cc = Counter()
        res = []
        cur = -1
        for i, ch in enumerate(s):
            heapq.heappush(q,(ch,i))
            if i == mp[ch] and cc[ch] == 0:
                while q:
                    ch2, j = heapq.heappop(q)
                    if j <= cur or cc[ch2] == 1:
                        continue
                    res.append(ch2)
                    cc[ch2] += 1
                    cur = j
                    if ch2 == ch:
                        break
                # print(i,ch,res)            
        return ''.join(res)




class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        alphas = [chr(ord('a')+i) for i in range(26)]
        mp = defaultdict(deque)
        res = []
        cc = Counter()
        cur = -1
        for i, ch in enumerate(s):
            mp[ch].append(i)
        for i, ch in enumerate(s):
            if i == mp[ch][-1] and cc[ch] == 0:
                for a in alphas:
                    if cc[a] == 1:
                        continue
                    while mp[a] and mp[a][0] <= cur:
                        mp[a].popleft()
                    if mp[a] and mp[a][0] <= i:
                        res.append(a)
                        cc[a] += 1
                        cur = mp[a][0]
                        if a == ch:
                            break
                # print(cur,i,ch,res)
        return ''.join(res)


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        mp = {ch:i for i, ch in enumerate(s)}
        q = deque()
        res = []
        for i, ch in enumerate(s):
            if (ch not in q) and (ch not in res):
                while q and q[-1] > ch:
                    q.pop()
                q.append(ch)
            # print(i,ch,q,res)
            while (ch not in res) and mp[ch] == i:
                ch2 = q.popleft()
                if ch2 not in res:
                    res.append(ch2)
        return ''.join(res)


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        mp = {ch:i for i, ch in enumerate(s)}
        q = deque()
        res = []
        for i, ch in enumerate(s):
            if ch in res:
                continue
            if ch not in q:
                while q and q[-1] > ch:
                    q.pop()
                q.append(ch)
            
            # print(i,ch,q,res)
            while (ch not in res) and mp[ch] == i:
                ch2 = q.popleft()
                if ch2 not in res:
                    res.append(ch2)
        return ''.join(res)





# from collections import Counter

# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:

#         # find pos - the index of the leftmost letter in our solution
#         # we create a counter and end the iteration once the suffix doesn't have each unique character
#         # pos will be the index of the smallest character we encounter before the iteration ends
#         c = Counter(s)
#         pos = 0
#         for i in range(len(s)):
#             if s[i] < s[pos]: pos = i
#             c[s[i]] -=1
#             if c[s[i]] == 0: break
#         # our answer is the leftmost letter plus the recursive call on the remainder of the string
#         # note we have to get rid of further occurrences of s[pos] to ensure that there are no duplicates
#         return s[pos] + self.removeDuplicateLetters(s[pos:].replace(s[pos], "")) if s else ''


class Solution:
    def removeDuplicateLetters(self, s) -> int:

        stack = []

        # this lets us keep track of what's in our solution in O(1) time
        seen = set()

        # this will let us know if there are no more instances of s[i] left in s
        last_occurrence = {c: i for i, c in enumerate(s)}


        for i, c in enumerate(s):

            # we can only try to add c if it's not already in our solution
            # this is to maintain only one of each character
            if c not in seen:
                # if the last letter in our solution:
                #    1. exists
                #    2. is greater than c so removing it will make the string smaller
                #    3. it's not the last occurrence
                # we remove it from the solution to keep the solution optimal
                while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
        return ''.join(stack)


    def smallestSubsequence(self, S):
        last = {c: i for i, c in enumerate(S)}
        stack = []
        for i, c in enumerate(S):
            if c in stack: continue
            while stack and stack[-1] > c and i < last[stack[-1]]:
                stack.pop()
            stack.append(c)
        return "".join(stack)