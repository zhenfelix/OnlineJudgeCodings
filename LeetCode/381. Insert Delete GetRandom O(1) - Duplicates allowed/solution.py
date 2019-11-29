class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.st = []
        self.mp = collections.defaultdict(list)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        flag = len(self.mp[val]) == 0
        self.mp[val].append(len(self.st))
        self.st.append((val,len(self.mp[val])-1))
        return flag 


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if len(self.mp[val]) == 0:
            return False
        idx = self.mp[val].pop()
        if idx != len(self.st)-1:
            self.st[idx] = self.st[-1]
            self.mp[self.st[idx][0]][self.st[idx][1]] = idx
        self.st.pop()
        return True

    def getRandom(self) -> int:
        """.
        Get a random element from the set.
        """
        idx = random.randint(0,len(self.st)-1)
        return self.st[idx][0]
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()