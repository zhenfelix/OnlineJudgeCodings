# class Solution:
#     def reverseWords(self, s: str) -> str:
#         return " ".join(s.split()[::-1])
        
    
class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(left, right):
            while left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            return
        
        n = len(s)
        arr = []
        idx, left, right = 0, 0, 0
        while idx < n:
            left = len(arr)
            while idx < n and s[idx] != ' ':
                arr.append(s[idx])
                idx += 1
            right = len(arr)
            if right > left:
                reverse(left,right-1)
                arr.append(" ")
            idx += 1
            
        reverse(0,len(arr)-1)
        
        if not arr:
            return ""
        return "".join(arr[1:])
        