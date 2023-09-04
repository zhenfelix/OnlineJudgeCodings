class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        mp = {pow(2,i) : i for i in range(32)}
        cnt = [0]*32
        for v in nums:
            cnt[mp[v]] += 1
        target = list(map(int,list(bin(target)[2:])))[::-1]
        m = len(target)
        # print(target,cnt)
        ans = 0
        for i in range(32):
            if i > 0:
                cnt[i] += cnt[i-1]//2
            if i < m and target[i]:
                if cnt[i] > 0:
                    cnt[i] -= 1
                    continue
                flag = False
                for j in range(i,32):
                    if cnt[j]:
                        flag = True
                        for k in range(i,j):
                            cnt[k] += 1
                        cnt[j] -= 1
                        ans += j-i
                        break 
                if not flag:
                    return -1
        return ans 