class Solution:
    def reversePairs(self, arr: List[int]) -> int:
        if not arr:
            return 0
        cnt, n, left, right = 0, len(arr), [], []
        idx = random.randint(0,n-1)
        for i, a in enumerate(arr):
            if i == idx:
                continue
            elif a <= arr[idx]:
                left.append(a)
                cnt += len(right)
                cnt += (a < arr[idx] and i > idx)
            else:
                right.append(a)
                cnt += (i < idx)
        cnt += self.reversePairs(left)
        cnt += self.reversePairs(right)
        return cnt

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        tmp = [0]*len(nums)
        def merge(left,right):
            
            if left >= right:
                return 0
            mid = (left+right)//2
            cnt = 0
            cnt += merge(left,mid)
            cnt += merge(mid+1,right)
            i, j = left, mid+1
            # print(left,right,cnt)
            for k in range(left,right+1):
                if i <= mid and (j > right or nums[i] <= nums[j]):
                    tmp[k] = nums[i]
                    cnt += j-mid-1
                    # print(i,j)
                    i += 1
                else:
                    tmp[k] = nums[j]
                    j += 1
            for k in range(left,right+1):
                nums[k] = tmp[k]
            # print(left,right,cnt)
            return cnt
        return merge(0,len(nums)-1)


class Solution:
    def reversePairs(self, arr: List[int]) -> int:
        def merge(left,right):
            if left >= right:
                return 0
            cnt = 0
            mid = (left+right)//2
            cnt += merge(left,mid)
            cnt += merge(mid+1,right)
            i, j = left, mid+1
            tmp = []
            while i <= mid or j <= right:
                if i > mid:
                    tmp += arr[j:right+1]
                    break
                if j > right:
                    tmp += arr[i:mid+1]
                    break
                if arr[i] <= arr[j]:
                    tmp.append(arr[i])
                    i += 1
                else:
                    tmp.append(arr[j])
                    j += 1
                    cnt += mid-i+1
            for i in range(left,right+1):
                arr[i] = tmp[i-left]
            return cnt
        return merge(0,len(arr)-1)



class Solution:
    def update(self, tree, pos, val):
        n = len(tree)-1
        while pos <= n:
            tree[pos] += val
            pos += (pos & (-pos))
        return

    def sums(self, tree, pos):
        res = 0
        while pos > 0:
            res += tree[pos]
            pos -= (pos & (-pos))
        return res

    def query(self, tree, left, right):
        return self.sums(tree,right)-self.sums(tree,left-1)


    def reversePairs(self, nums: List[int]) -> int:
        arr = sorted(set(nums))[::-1]
        n = len(arr)
        mp = {}
        for i, a in enumerate(arr):
            mp[a] = i + 1
        cnt = [0]*(n+1)
        ans = 0
        for num in nums:
            # ans += self.query(cnt,mp[num]+1,n)
            ans += self.sums(cnt,mp[num]-1)
            self.update(cnt,mp[num],1)
        
        return ans
