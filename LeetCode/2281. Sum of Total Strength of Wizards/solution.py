class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        n = len(strength)
        # left[i] 为左侧严格小于 strength[i] 的最近元素位置（不存在时为 -1）
        # right[i] 为右侧小于等于 strength[i] 的最近元素位置（不存在时为 n）
        left, right, st = [-1] * n, [n] * n, []
        for i, v in enumerate(strength):
            while st and strength[st[-1]] >= v: right[st.pop()] = i
            if st: left[i] = st[-1]
            st.append(i)

        ss = list(accumulate(accumulate(strength, initial=0), initial=0))  # 前缀和的前缀和

        ans = 0
        for i, v in enumerate(strength):
            l, r = left[i] + 1, right[i] - 1  # [l, r]  左闭右闭
            tot = (i - l + 1) * (ss[r + 2] - ss[i + 1]) - (r - i + 1) * (ss[i + 1] - ss[l])
            ans += v * tot  # 累加贡献
        return ans % (10 ** 9 + 7)


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/sum-of-total-strength-of-wizards/solution/dan-diao-zhan-qian-zhui-he-de-qian-zhui-d9nki/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        def update(diff, left, right, val):
            diff[left] += val
            diff[right+1] -= val

        st = [-1]
        MOD = 10**9+7
        n = len(strength)
        strength.append(0)
        sums = [0]*len(strength)
        muls = [0]*len(strength)
        for i, s in enumerate(strength):
            while st and strength[st[-1]] > s:
                mid = st.pop()
                v = strength[mid]
                L, R = st[-1], i 
                # print(L,mid,R)
                update(sums, mid, mid, v*(mid-L)*(R-mid))
                update(sums, L+1, mid-1, -v*L*(R-mid))
                update(muls, L+1, mid-1, v*(R-mid))
                update(sums, mid+1, R-1, v*(mid-L)*R)
                update(muls, mid+1, R-1, -v*(mid-L))
            st.append(i)
        ans, cursum, curmul = 0, 0, 0
        # print(sums,muls)
        for i in range(n):
            cursum += sums[i]
            curmul += muls[i]
            ans += strength[i]*(cursum+curmul*i)
            ans %= MOD
        return ans





class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        MOD = 10**9+7
        strength.append(0)
        n = len(strength)
        st = [-1]
        ans = [0]*(n-1)

        sums = [0]*(n+10)
        mults = [0]*(n+10)

        def update(arr, idx, val):
            while idx < len(arr):
                arr[idx] += val
                idx += idx&(-idx)

        def range_update(arr, lo, hi, val):
            lo += 1
            hi += 1 
            update(arr, lo, val)
            update(arr, hi+1, -val)

        def query(arr, idx):
            idx += 1 
            tot = 0
            while idx > 0:
                tot += arr[idx]
                idx -= idx&(-idx)
            return tot 


        for i, s in enumerate(strength):
            while st and strength[st[-1]] > s:
                idx = st.pop()
                v = strength[idx]
                L, R = idx-st[-1]-1, i-idx-1
                # print(st[-1],idx,i,L,R)
                ans[idx] += (L+1)*(R+1)*v
                ans[idx] %= MOD
                if L > 0:
                    range_update(sums, st[-1]+1, idx-1, -st[-1]*(R+1)*v)
                    range_update(mults, st[-1]+1, idx-1, (R+1)*v)
                if R > 0:
                    range_update(sums, idx+1, i-1, i*(L+1)*v)
                    range_update(mults, idx+1, i-1, -(L+1)*v)
                # print(sums,mults)
                # print(ans)
            st.append(i)

        res = 0
        for i in range(n-1):
            ans[i] += query(sums, i)
            ans[i] += query(mults, i)*i
            res += ans[i]*strength[i]
            res %= MOD
        # print(ans)
        return res



