class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        left, right = 0, len(removable)
        def get(arr):
            news = []
            arr = arr[::-1]
            for i, ch in enumerate(s):
                if arr and arr[-1] == i:
                    arr.pop()
                    continue
                news.append(ch)
            return news

        def isSub(news):
            news = news[::-1]
            for ch in p:
                while news and news[-1] != ch:
                    news.pop()
                if not news:
                    return False
                news.pop()
            return True


        # print(left,right)
        while left <= right:
            mid = (left+right)//2
            ss = get(sorted(removable[:mid]))
            # print(left,mid,right, removable[:mid], ss)
            if isSub(ss):
                left = mid + 1
            else:
                right = mid - 1
        return right




class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        ns, np = len(s), len(p)
        n = len(removable)
        # 辅助函数，用来判断移除 k 个下标后 p 是否是 s_k 的子序列
        def check(k: int) -> bool:
            state = [True] * ns   # s 中每个字符的状态
            for i in range(k):
                state[removable[i]] = False
            # 匹配 s_k 与 p 
            j = 0
            for i in range(ns):
                # s[i] 未被删除且与 p[j] 相等时，匹配成功，增加 j
                if state[i] and s[i] == p[j]:
                    j += 1
                    if j == np:
                        return True
            return False
        
        # 二分查找
        l, r = 0, n + 1
        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid
        return l - 1


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/maximum-number-of-removable-characters/solution/ke-yi-chu-zi-fu-de-zui-da-shu-mu-by-leet-9ve9/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。