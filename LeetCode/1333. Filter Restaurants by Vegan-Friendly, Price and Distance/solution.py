class Solution:
    # def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
    #     restaurants = sorted([(-rating, -id) for id, rating, vf, price, dis in restaurants if (not veganFriendly or vf) and (price <= maxPrice) and (dis <= maxDistance)])
    #     return [-id for r, id in restaurants]
    
    def filterRestaurants(self, A, veganFriendly, maxPrice, maxDistance):
        A.sort(key=lambda x: (-x[1], -x[0]))
        return [i for i, r, v, p, d in A if v >= veganFriendly and p <= maxPrice and d <= maxDistance]