class Solution:
    def convertToTitle(self, num: int) -> str:
        # n -= 1
        # mp = [chr(65+i) for i in range(26)]
        # res = ""
        # while n >= 0:
        #     res = mp[n%26]+res
        #     n = n//26
        #     n -= 1
        # return res
        
        return "" if num == 0 else self.convertToTitle((num - 1) // 26) + chr((num - 1) % 26 + ord('A'))

