class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        m = {}
        for name, id, view in zip(creators, ids, views):
            if name in m:
                t = m[name]
                t[0] += view
                if view > t[1] or view == t[1] and id < t[2]:
                    t[1], t[2] = view, id
            else:
                m[name] = [view, view, id]

        ans, max_view_sum = [], -1
        for name, (view_sum, max_view, id) in m.items():
            if view_sum > max_view_sum:
                max_view_sum = view_sum
                ans = [[name, id]]
            elif view_sum == max_view_sum:
                ans.append([name, id])
        return ans


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/most-popular-video-creator/solution/bian-li-by-endlesscheng-a77m/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        cc = Counter()
        n = len(creators)
        # cnt = Counter()
        # for i, v in zip(range(n), views):
        #     cnt[i] = v 
        for c, v in zip(creators, views):
            cc[c] += v 
        mx = max(cc.values())
        mp = dict()
        for c, i in zip(creators, range(n)):
            s = ids[i]
            if cc[c] == mx:
                if c not in mp or (views[mp[c]] < views[i] or (views[mp[c]] == views[i] and s < ids[mp[c]])):
                    mp[c] = i
        # print(cnt["fhcw"],cnt["f"])
        # print(n,len(cnt))
        return [[k,ids[v]] for k, v in mp.items()]