class Solution:
    def countPairs(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        cnt = defaultdict(int)
        for x in nums:
            st = {x}  # 不交换
            s = list(str(x))
            m = len(s)
            for i in range(m):
                for j in range(i + 1, m):
                    s[i], s[j] = s[j], s[i]
                    st.add(int(''.join(s)))  # 交换一次
                    for p in range(i + 1, m):
                        for q in range(p + 1, m):
                            s[p], s[q] = s[q], s[p]
                            st.add(int(''.join(s)))  # 交换两次
                            s[p], s[q] = s[q], s[p]
                    s[i], s[j] = s[j], s[i]
            ans += sum(cnt[v] for v in st)
            cnt[x] += 1
        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/count-almost-equal-pairs-ii/solutions/2892072/pai-xu-mei-ju-you-wei-hu-zuo-pythonjavac-vbg0/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。