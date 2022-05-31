class DiscountSystem:

    def __init__(self):
        self.activity = defaultdict(list)
        self.ucnt = defaultdict(int)


    def addActivity(self, actId: int, priceLimit: int, discount: int, number: int, userLimit: int) -> None:
        self.activity[actId] = [priceLimit,discount,userLimit,number]

    def removeActivity(self, actId: int) -> None:
        if actId in self.activity:
            del self.activity[actId]


    def consume(self, userId: int, cost: int) -> int:
        candidates = [(-d,actId) for actId, (p,d,u,n) in self.activity.items() if cost >= p and self.ucnt[userId,actId] < u]
        if not candidates:
            return cost
        d, actId = min(candidates)
        self.ucnt[userId,actId] += 1
        self.activity[actId][-1] -= 1
        if self.activity[actId][-1] == 0:
            del self.activity[actId]
        return cost+d


# Your DiscountSystem object will be instantiated and called as such:
# obj = DiscountSystem()
# obj.addActivity(actId,priceLimit,discount,number,userLimit)
# obj.removeActivity(actId)
# param_3 = obj.consume(userId,cost)