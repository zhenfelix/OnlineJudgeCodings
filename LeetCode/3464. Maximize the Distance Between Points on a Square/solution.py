import bisect
from typing import List

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # Convert points to their perimeter coordinates
        coordinates = []
        for x, y in points:
            if y == 0:  # Bottom edge
                coord = x
            elif x == side:  # Right edge
                coord = side + y
            elif y == side:  # Top edge
                coord = 2 * side + (side - x)
            else:  # Left edge (x == 0)
                coord = 3 * side + (side - y)
            coordinates.append(coord)
        
        coordinates.sort()
        n = len(coordinates)
        if n < k:
            return 0  # Not enough points, though the problem states k <= points.length

        perimeter = 4 * side
        coordinates += [x+perimeter for x in coordinates]
        
        # Binary search for the maximum possible minimum distance
        low, high = 0, 2 * side
        best = 0
        # print(coordinates)
        while low <= high:
            mid = (low + high) // 2
            if self.is_possible(coordinates, mid, k, side):
                best = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return high
    
    def is_possible(self, arr: List[int], d: int, k: int, side: int) -> bool:
        perimeter = 4 * side
        n = len(arr)//2
        for i in range(n):
            current = arr[i]
            next_pos = current
            for _ in range(k - 1):
                target = next_pos + d
                j = bisect.bisect_left(arr, target)
                if j < n*2:
                    if j >= n and j%n >= i:
                        # print(arr,d,1,i,j)
                        return False
                    next_pos = arr[j]
                else:
                    # print(arr,d,2)
                    return False
            if (arr[i] + perimeter - next_pos) >= d:
                return True
        print(arr,d)
        return False