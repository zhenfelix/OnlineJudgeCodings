# Problem Statement
# As a result of ever increasing traffic jams, subway transportation in big cities has become a must. A train can actually take you from your home to your office faster than a car can. But what happens if you have your office in another city? In this problem we consider three different cities: A, B and C. Each of these cities has its own subway transportation system and you can go from a station to any other in the same city without having to leave the underground. A big project is now underway, and the goal is to merge the subway lines such that transportation between these cities becomes available soon. In order to achieve this, it was decided that two tunnels would be constructed, each of them connecting two subway stations in two different cities. This has to be done at a minimal cost, so it is important which subway stations are chosen. Also consider that the only factor in determining the cost is the distance between the two subway stations connected by a tunnel.

# You will be given a int[] ax, a int[] ay, a int[] bx, a int[] by, a int[] cx and a int[] cy with the following signification:
# ax and ay represent the coordinates of the subway stations in city A i.e (ax[i],ay[i]) is the point denoting the place of the i-th station
# bx and by represent the coordinates of the subway stations in city B i.e (bx[i],by[i]) is the point denoting the place of the i-th station
# cx and cy represent the coordinates of the subway stations in city C i.e (cx[i],cy[i]) is the point denoting the place of the i-th station

# Return the minimal added distance of the two tunnels such that all three cities become connected.


class ATaleOfThreeCities:
    def bestPair(self, x1, y1, x2, y2):
        dis = float('inf')
        for xy1 in zip(x1, y1):
            for xy2 in zip(x2, y2):
                dis = min(dis, ((xy1[0]-xy2[0])**2+(xy1[1]-xy2[1])**2)**0.5)
        return dis


    def connect(self, ax, ay, bx, by, cx, cy):
        AB = self.bestPair(ax, ay, bx, by)
        BC = self.bestPair(bx, by, cx, cy)
        AC = self.bestPair(ax, ay, cx, cy)
        return AB+BC+AC-max(AB,AC,BC)