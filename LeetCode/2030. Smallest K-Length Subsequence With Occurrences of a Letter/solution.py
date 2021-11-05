贪心stack
class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        n = len(s)
        st = []
        cnt = 0
        remains = sum(ch == letter for ch in s)
        for i, ch in enumerate(s):
            # print(i,ch,st,remains)
            while st and st[-1] > ch and len(st)+n-i > k and remains-(st[-1]==letter) >= repetition:
                remains -= (st[-1]==letter)
                st.pop()
            st.append(ch)
        r = repetition-sum(ch == letter for ch in st[:k])
        # print(st)
        for i in range(k)[::-1]:
            if r > 0 and st[i] != letter:
                st[i] = letter
                r -= 1

        return ''.join(st[:k])







先来考虑几个简单的问题
1。从s中找出字典序最小的字符，显然就是在s的全部范围内找出最小的字符
2。从s中找出字典序最小的长度为k的子序列，我们希望在尽可能大的范围里面依次找最小的字符，那么对子序列里的第一个字符显然最大的范围是s[:-k]，因为如果最小值恰好是s[-k+1]，那么剩下的字符不足以填k-1位置了，依次往后我们可以用单调队列维护这个动态区间的最小值
3。从s中找出字典序最小的包含repetition个letter的子序列，我们首先用ls数组依次记录letter出现的下标，同样可以采用2。的逻辑，在尽可能大的范围里面找最小字符，那么临界状态就是ls[-repetition]的位置，这里有一个细节，在ls[-repetition]和ls[-repetition+1]之间可能还有其他字符，为什么临界位置不是他们？（如果这些字符大于letter，那么最小字符自然不会是他们，无需考虑；如果这些字符小于letter，那么ls[-repetition]位置的letter会被忽略，那么最终的letter数量会小于repetition）
4。所以在该问题中，我们需要同时考虑2。和3。的临界条件，任意一个临界条件满足的时候，我们就需要找出当前范围的最小值。但是这里还隐含里一个临界条件，当临界条件3。满足的时候，我们在当前范围的最小值可能不是letter，那么无法消除临界条件，那么将不断轮回寻找当前范围最小值，这时k会变小但是repetition不变，于是会遇到新的临界条件repetition==k，那么下一个最小值就必须是letter，否则剩下的空位k<repetition会导致矛盾
class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        n = len(s)
        ls = [i for i, ch in enumerate(s) if ch == letter]
        q = deque()
        res = []
        for i, ch in enumerate(s):
            while q and s[q[-1]] > ch:
                q.pop()
            q.append(i)
            
            while n-i == k or (repetition > 0 and i == ls[-repetition]):
            # while q and (n-i == k or i == ls[-repetition]):
                j = q.popleft()
                if k > 0 and (k > repetition or s[j] == letter):
                    # print(i,s[j])
                    res.append(s[j])
                    k -= 1
                    repetition -= (res[-1] == letter)

        return ''.join(res)



class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        mp = defaultdict(deque)
        for i, ch in enumerate(s):
            mp[ch].append(i)
        alphas = [chr(ord('a')+i) for i in range(26)]
        n = len(s)
        res = []
        sz = k
        cur = -1
        for _ in range(sz):
            for ch in alphas:
                # if repetition == k and ch != letter:
                #     continue
                while mp[ch] and mp[ch][0] <= cur:
                    mp[ch].popleft()
                if mp[ch] and mp[ch][0] <= n-k and repetition-(ch==letter) <= k-1 and (repetition <= 0 or mp[ch][0] <= mp[letter][-repetition]):
                    res.append(ch)
                    cur = mp[ch][0]
                    mp[ch].popleft()
                    k -= 1
                    if ch == letter:
                        repetition -= 1
                    break
        return ''.join(res)



class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        mp = defaultdict(deque)
        for i, ch in enumerate(s):
            mp[ch].append(i)
        alphas = [chr(ord('a')+i) for i in range(26)]
        n = len(s)
        res = []
        sz = k
        cur = -1
        for _ in range(sz):
            for ch in alphas:
                if repetition == k and ch != letter:
                    continue
                while mp[ch] and mp[ch][0] <= cur:
                    mp[ch].popleft()
                if mp[ch] and mp[ch][0] <= n-k and (repetition <= 0 or mp[ch][0] <= mp[letter][-repetition]):
                    res.append(ch)
                    cur = mp[ch][0]
                    mp[ch].popleft()
                    k -= 1
                    if ch == letter:
                        repetition -= 1
                    break
        return ''.join(res)