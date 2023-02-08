class Solution:
    def stoneGameVI(self, A, B):
        A = sorted(zip(A, B), key=sum)
        return cmp(sum(a for a, b in A[::-2]), sum(b for a, b in A[-2::-2]))


class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        arr = [(a+b,a,b) for a, b in zip(aliceValues,bobValues)]
        arr.sort(reverse = True)
        alice, bob = 0, 0
        for i in range(len(arr)):
            _, a, b = arr[i]
            if i&1:
                bob += b 
            else:
                alice += a 
        if alice > bob:
            return 1
        elif alice == bob:
            return 0
        return -1
