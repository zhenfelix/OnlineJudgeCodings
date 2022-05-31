class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.keys = keys
        self.values = values
        self.mp = {k : i for i, k in enumerate(keys)}
        self.cnt = defaultdict(int)
        for word in dictionary:
            self.cnt[self.encrypt(word)] += 1


    def encrypt(self, word1: str) -> str:
        return ''.join([self.values[self.mp[w]] for w in word1])


    def decrypt(self, word2: str) -> int:
        return self.cnt[word2]



# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)




class Encrypter(object):

    def __init__(self, keys, values, dictionary):
        self.enc = {k: v for k,v in zip(keys, values)}
        self.decrypt = collections.Counter(self.encrypt(w) for w in dictionary).__getitem__

    def encrypt(self, word1):
        return ''.join(self.enc.get(c, '#') for c in word1)