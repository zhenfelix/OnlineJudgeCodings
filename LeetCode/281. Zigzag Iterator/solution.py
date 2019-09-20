class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v = [v1,v2]
        self.row = 0
        self.cols = [0]*len(self.v)

    def next(self):
        """
        :rtype: int
        """
        res = self.v[self.row][self.cols[self.row]]
        self.cols[self.row] += 1
        self.row += 1
        self.row %= len(self.v)
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        for i in range(len(self.v)):
            if self.cols[self.row] < len(self.v[self.row]):
                return True
            self.row += 1
            self.row %= len(self.v)
        return False
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())