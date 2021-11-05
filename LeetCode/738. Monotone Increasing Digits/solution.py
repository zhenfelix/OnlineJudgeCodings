class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        arr = list(str(n))
        m = len(arr)
        pre = '0'
        flag = True
        for i, a in enumerate(arr):
            if a < pre and flag:
                flag = False
                j = i-1
                while j > 0 and arr[j-1] == arr[j]:
                    j -= 1
                arr[j] = str(int(arr[j])-1)
                # print(j,arr[j])
                j += 1
                while j < i:
                    arr[j] = '9'
                    j += 1
            if not flag:
                arr[i] = '9'
            pre = arr[i]
            print(i,a,arr)
        return int(''.join(arr))
