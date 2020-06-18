class Solution:
    # def finalPrices(self, prices: List[int]) -> List[int]:
    #     st = [0]
    #     n = len(prices)
    #     for i in range(n)[::-1]:
    #         while st and st[-1] > prices[i]:
    #             st.pop()
    #         tmp = prices[i]
    #         prices[i] -= st[-1]
    #         st.append(tmp)
    #     return prices
    
    def finalPrices(self, A):
        stack = []
        for i, a in enumerate(A):
            while stack and A[stack[-1]] >= a:
                A[stack.pop()] -= a
            stack.append(i)
        return A