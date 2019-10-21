class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        cnt = len(strs)
        cnts = [str(len(strs[i])) for i in range(cnt)]
        return ' '.join([str(cnt)]+cnts) + ' ' +''.join(strs)
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        tmp = s.split(' ')
        cnt = int(tmp[0])
        cnts = [int(tmp[i+1]) for i in range(cnt)]
        res = []
        s = ' '.join(tmp[cnt+1:])
        cur = 0
        for i in cnts:
            res.append(s[cur:cur+i])
            cur += i
        return res
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))