class Solution:
    def isSelfCrossing(self, arr: List[int]) -> bool:
        q = deque([0,0,0,0])
        contract = False
        for x in arr:
            if contract:
                if x >= q[-2]:
                    return True
            else:
                if x <= q[-2]:
                    if x >= q[-2] - q[-4]:
                        q[-1] -= q[-3]
                    contract = True
            q.append(x)
            if len(q) > 4:
                q.popleft()
        return False


class Solution:
    def isSelfCrossing(self, arr: List[int]) -> bool:
        contract = False
        n = len(arr)
        arr.extend([0,0,0,0])
        for i, x in enumerate(arr):
            if i == n:
                break
            if contract:
                if x >= arr[i-2]:
                    return True
            else:
                if x <= arr[i-2]:
                    if x >= arr[i-2] - arr[i-4]:
                        arr[i-1] -= arr[i-3]
                    contract = True
        return False