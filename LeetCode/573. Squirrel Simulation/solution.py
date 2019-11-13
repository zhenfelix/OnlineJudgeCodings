class Solution(object):
    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        dis1 = [abs(nut[0]-tree[0])+abs(nut[1]-tree[1]) for nut in nuts]
        dis2 = [abs(nut[0]-squirrel[0])+abs(nut[1]-squirrel[1]) for nut in nuts]
        idx = min(range(len(dis1)), key = lambda x: dis2[x]-dis1[x])
        return sum(dis1)*2 + dis2[idx] - dis1[idx]