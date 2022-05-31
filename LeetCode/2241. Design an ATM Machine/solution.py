class ATM:

    def __init__(self):
        self.cnt = [0]*5
        self.val = [20,50,100,200,500]


    def deposit(self, banknotesCount: List[int]) -> None:
        for i, x in enumerate(banknotesCount):
            self.cnt[i] += x


    def withdraw(self, amount: int) -> List[int]:
        now = [0]*5
        for i in range(5)[::-1]:
            delta = amount//self.val[i]
            now[i] = min(delta, self.cnt[i])
            amount -= self.val[i]*now[i]
        if amount > 0:
            return [-1]
        for i in range(5):
            self.cnt[i] -= now[i]
        return now



# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
