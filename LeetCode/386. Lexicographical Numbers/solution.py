class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def preOrder(cur):
            if cur > n:
                return
            res.append(cur)
            preOrder(cur*10)
            if (cur+1) %10 != 0: preOrder(cur+1)
            return
        
        res = []
        preOrder(1)
        return res
    
    
# class Solution:
#     def lexicalOrder(self, n: int) -> List[int]:
#          return sorted(range(1, n+1), key=str)


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def preOrder(cur):
            if cur > n:
                return
            res.append(cur)
            for i in range(10):
                preOrder(cur*10+i)
            return
        
        res = []
        for root in range(1,10):
            preOrder(root)
        return res