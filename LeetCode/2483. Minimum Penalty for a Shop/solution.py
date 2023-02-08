class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        t, cost = 0, customers.count('Y')
        pre, suf = 0, cost
        for i in range(n):
            if customers[i] == 'N':
                pre += 1
            else:
                suf -= 1
            if pre+suf < cost:
                t, cost = i+1, pre+suf
        return t 