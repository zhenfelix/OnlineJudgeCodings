class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.cnt, self.n, self.discount = 0, n, discount
        self.id2p = {}
        for id, price in zip(products,prices):
            self.id2p[id] = price

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.cnt += 1
        flag = self.cnt%self.n == 0
        sums = 0
        for id, amt in zip(product,amount):
            sums += self.id2p[id]*amt
        return sums*(100-self.discount*flag)/100

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)