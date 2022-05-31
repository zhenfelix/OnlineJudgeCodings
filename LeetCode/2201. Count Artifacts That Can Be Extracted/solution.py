class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        m = len(artifacts)
        cnt = [0]*m  
        mp = dict()
        for i, (r1,c1,r2,c2) in enumerate(artifacts):
            for r in range(r1,r2+1):
                for c in range(c1,c2+1):
                    mp[r,c] = i 
                    cnt[i] += 1 
        for r, c in dig:
            if (r,c) in mp:
                idx = mp[r,c]
                cnt[idx] -= 1
        return sum(c == 0 for c in cnt)


class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        d = set(map(tuple, dig))
        return len([1 for r1, c1, r2, c2 in artifacts if all((r, c) in d for r in range(r1, r2 + 1) for c in range(c1, c2 + 1))])


# 作者：吴自华
# 链接：https://leetcode-cn.com/circle/discuss/3PMerp/view/yboIva/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。