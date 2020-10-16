class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.alive = set([kingName])
        self.children = defaultdict(list)


    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)
        self.alive.add(parentName)
        self.alive.add(childName)


    def death(self, name: str) -> None:
        self.alive.remove(name)


    def getInheritanceOrder(self) -> List[str]:
        curOrder = []
        def dfs(x):
            if x in self.alive:
                curOrder.append(x)
            for nxt in self.children[x]:
                dfs(nxt)
            return
        dfs(self.king)
        return curOrder






# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()