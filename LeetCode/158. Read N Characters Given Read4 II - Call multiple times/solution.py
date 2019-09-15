"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def __init__(self):
        self.virtualIdx = 0
        self.virtualSz = 0
        self.init = True
        self.tmp = ['']*4
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        if self.init:
            self.virtualSz += read4(self.tmp)
            self.init = False
        cur = 0
        while cur < n and self.virtualIdx < self.virtualSz:
            buf[cur] = self.tmp[self.virtualIdx%4]
            cur += 1
            self.virtualIdx += 1
            if self.virtualIdx%4 == 0:
                self.virtualSz += read4(self.tmp)
        return cur
            