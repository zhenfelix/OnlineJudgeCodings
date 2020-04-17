class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        for i in range(1,int((num+2)**0.5)+1)[::-1]:
            if (num+1)%i == 0:
                return [i,(num+1)//i]
            if (num+2)%i == 0:
                return [i,(num+2)//i]
        return [-1,-1]