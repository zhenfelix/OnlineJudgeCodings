class Solution:
    def maximumSwap(self, num: int) -> int:
        arr = list(str(num))
        mp = {int(ch):i for i, ch in enumerate(arr)}
        for i, ch in enumerate(arr):
            k = int(ch)
            for j in range(k+1,10)[::-1]:
                if j in mp and mp[j] > i:
                    arr[i], arr[mp[j]] = arr[mp[j]], arr[i]
                    return int(''.join(arr))
        return num



def maximumSwap(self, num):
    A = list(str(num))
    ans = A[:]
    for i in xrange(len(A)):
        for j in xrange(i+1, len(A)):
            A[i], A[j] = A[j], A[i]
            if A > ans: ans = A[:]
            A[i], A[j] = A[j], A[i]

    return int("".join(ans))