class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        mx, my = max(cx + cr for cx, cy, cr in circles) + 2, max(cy + cr for cx, cy, cr in circles) + 1
        diffs = [[0] * mx for _ in range(my)]
        for cx, cy, cr in circles:
            for y in range(cy - cr, cy + cr + 1):
                z = isqrt(cr * cr - (y - cy) ** 2)
                diffs[y][cx - z] += 1
                diffs[y][cx + z + 1] -= 1
        return sum(sum(cur > 0 for cur in accumulate(xs)) for xs in diffs)


# 作者：FreeYourMind
# 链接：https://leetcode-cn.com/problems/count-lattice-points-inside-a-circle/solution/by-freeyourmind-bftz/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        ans = set()
        for xx,yy,rr in circles:
            for x in range(xx-rr,xx+rr+1):
                for y in range(yy-rr,yy+rr+1):
                    if (x-xx)*(x-xx)+(y-yy)*(y-yy) <= rr*rr:
                        ans.add((x,y))
        return len(ans)



class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        ans = 0
        # print(len(circles))
        mx = max(max(c) for c in circles)
        mx *= 2
        for x in range(mx+1):
            for y in range(mx+1):
                if any((x-xx)*(x-xx)+(y-yy)*(y-yy) <= rr*rr for xx,yy,rr in circles):
                    ans += 1 
        return ans
