class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        n = len(s)
        arr = list(s)
        cnt = 0
        left, right = 0, n-1
        while left < right:
            i = left
            while arr[i] != arr[right]:
                i += 1
            j = right
            while arr[j] != arr[left]:
                j -= 1
            if i-left <= right-j:
                k = i 
                while k > left:
                    arr[k], arr[k-1] = arr[k-1], arr[k]
                    k -= 1
                cnt += i-left
            else:
                k = j
                while k < right:
                    arr[k], arr[k+1] = arr[k+1], arr[k]
                    k += 1
                cnt += right-j
            left += 1
            right -= 1
            # print(arr[left:right+1])
        return cnt