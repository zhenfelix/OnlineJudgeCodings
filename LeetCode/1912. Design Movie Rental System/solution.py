import bisect

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.movie_shop2price = {}
        self.movie2price_shop = defaultdict(list)
        self.price_shop_movie = []
        for s, m, p in entries:
            self.movie_shop2price[m,s] = p 
            self.movie2price_shop[m].append((p,s))
        for k, v in self.movie2price_shop.items():
            self.movie2price_shop[k].sort()

    def search(self, movie: int) -> List[int]:
        arr = self.movie2price_shop[movie][:5]
        return [s for p,s in arr]


    def rent(self, shop: int, movie: int) -> None:
        price = self.movie_shop2price[movie,shop]
        arr = self.movie2price_shop[movie]
        del arr[bisect.bisect_left(arr, (price,shop))]
        arr = self.price_shop_movie
        bisect.insort(arr, (price,shop,movie))



    def drop(self, shop: int, movie: int) -> None:
        price = self.movie_shop2price[movie,shop]
        arr = self.price_shop_movie
        del arr[bisect.bisect_left(arr, (price,shop,movie))]
        arr = self.movie2price_shop[movie]
        bisect.insort(arr, (price,shop))


    def report(self) -> List[List[int]]:
        arr = self.price_shop_movie[:5]
        return [[s,m] for p,s,m in arr]



# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()



from sortedcontainers import SortedSet
class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.s = {}
        self.p = {}
        for shop, movie, price in entries:
            if movie not in self.s:
                self.s[movie] = SortedSet()
            self.s[movie].add((price, shop))
            self.p[(shop, movie)] = price
        self.foo = SortedSet()

    def search(self, movie: int) -> List[int]:
        if movie in self.s:
            return [i[1] for i in self.s[movie][:5]]
        return []

    def rent(self, shop: int, movie: int) -> None:
        price = self.p[(shop, movie)]
        self.s[movie].remove((price, shop))
        self.foo.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.p[(shop, movie)]
        self.s[movie].add((price, shop))
        self.foo.remove((price, shop, movie))

    def report(self) -> List[List[int]]:
        return [(i[1], i[2]) for i in self.foo[:5]]



# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()


from collections import defaultdict
from typing import List
from sortedcontainers import SortedList


class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.price = {}
        self.unrented = defaultdict(SortedList)
        self.rented = SortedList()
        for shop, movie, price in entries:
            self.price[(shop, movie)] = price
            self.unrented[movie].add((price, shop))

    def search(self, movie: int) -> List[int]:
        li = self.unrented[movie]
        if len(li) < 5:
            return [shop for _, shop in li]
        return [shop for _, shop in li[:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.price[(shop, movie)]
        self.unrented[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.price[(shop, movie)]
        self.unrented[movie].add((price, shop))
        self.rented.remove((price, shop, movie))

    def report(self) -> List[List[int]]:
        if len(self.rented) < 5:
            return [[shop, movie] for _, shop, movie in self.rented]
        return [[shop, movie] for _, shop, movie in self.rented[:5]] 


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()