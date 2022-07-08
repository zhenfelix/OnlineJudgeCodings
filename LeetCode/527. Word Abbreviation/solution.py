class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.cnt = Counter()

class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        m = len(word)
        cur = self.root
        for i, ch in enumerate(word):
            cur.cnt[m-i] += 1
            cur = cur.children[ch]

    def query(self, word):
        m = len(word)
        cur = self.root
        sz = 0
        for ch in word:
            if cur.cnt[m-sz] == 1:
                break
            cur = cur.children[ch]
            sz += 1
        sz = max(sz,1)
        if sz >= m-1:
            return word
        # if sz == 0:
        #     return word[0]+str(m-1)
        return word[:sz]+str(m-sz)

class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        mp = defaultdict(Trie)
        for word in words:
            mp[word[-1]].add(word[:-1])
        ans = []
        for word in words:
            q = mp[word[-1]].query(word[:-1])
            ans.append(q+word[-1])
        return ans




class Solution(object):
    def wordsAbbreviation(self, words):
        groups = collections.defaultdict(list)
        for index, word in enumerate(words):
            groups[len(word), word[0], word[-1]].append((word, index))

        ans = [None] * len(words)
        Trie = lambda: collections.defaultdict(Trie)
        COUNT = False
        for k, group in groups.items():
            trie = Trie()
            for word, _ in group:
                cur = trie
                for letter in word[1:]:
                    cur[COUNT] = cur.get(COUNT, 0) + 1
                    cur = cur[letter]

            for word, index in group:
                cur = trie
                for i, letter in enumerate(word[1:], 1):
                    if cur[COUNT] == 1: break
                    cur = cur[letter]
                if len(word) - i - 1 > 1:
                    ans[index] = word[:i] + str(len(word) - i - 1) + word[-1]
                else:
                    ans[index] = word
        return ans


# 作者：LeetCode
# 链接：https://leetcode.cn/problems/word-abbreviation/solution/dan-ci-suo-xie-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。