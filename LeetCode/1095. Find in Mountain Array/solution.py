class Solution:
    def findInMountainArray(self, secret: List[int], target: int) -> int:
        def findPeak():
            n = len(secret)
            left, right = 0, n-2
            while left+1 < right:
                mid = (left+right)//2
                if secret[mid] < secret[mid+1]:
                    left = mid
                else:
                    right = mid
            return right
        
        peak = findPeak()
        
        # print(peak)
        
        left, right = 0, peak+1
        # if secret[right] == target:
        #     return right
        while left < right:
            mid = (left+right)//2
            if secret[mid] == target:
                return mid
            elif secret[mid] < target:
                left = mid+1
            else:
                right = mid
        
        left, right = peak, len(secret)
        # if secret[right] == target:
        #     return right
        while left < right:
            mid = (left+right)//2
            if secret[mid] == target:
                return mid
            elif secret[mid] > target:
                left = mid+1
            else:
                right = mid
                
        return -1
            
        