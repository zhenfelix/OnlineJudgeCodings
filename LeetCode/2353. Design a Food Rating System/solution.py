class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.rank = defaultdict(list)
        self.mp = dict()
        self.f2c = dict()
        for i, (f,c,r) in enumerate(zip(foods,cuisines,ratings)):
            heapq.heappush(self.rank[c], (-r,f))
            self.mp[f] = r
            self.f2c[f] = c 


    def changeRating(self, food: str, newRating: int) -> None:
        self.mp[food] = newRating
        cuisine = self.f2c[food]
        heapq.heappush(self.rank[cuisine], (-newRating,food))


    def highestRated(self, cuisine: str) -> str:
        while self.rank[cuisine] and self.mp[self.rank[cuisine][0][-1]] != -self.rank[cuisine][0][0]:
            heapq.heappop(self.rank[cuisine])
        return self.rank[cuisine][0][-1]



# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)