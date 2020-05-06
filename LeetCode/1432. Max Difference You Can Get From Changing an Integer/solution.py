class Solution:
    def maxDiff(self, num: int) -> int:
        num = str(num)
        maxNum, minNum = float('-inf'), float('inf')
        for i in '0123456789':
            for j in '0123456789':
                nextNum = num.replace(i, j)
                if nextNum[0] == '0' or int(nextNum) == 0:
                    continue
                maxNum = max(maxNum, int(nextNum))    
                minNum = min(minNum, int(nextNum))    
        return maxNum - minNum 



# class Solution:
#     def maxDiff(self, num: int) -> int:
#         num = str(num)
#         n = len(num)
#         idx = 0
#         while idx < n and num[idx] == '9':
#             idx += 1
#         a = num if idx == n else num.replace(num[idx],'9')
#         idx = 0
#         while idx < n and num[idx] in '01':
#             idx += 1
#         b = num if idx == n else num.replace(num[idx],'1' if idx == 0 else '0')
#         return int(a) - int(b)
            
        