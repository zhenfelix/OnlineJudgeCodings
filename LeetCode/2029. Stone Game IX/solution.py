等效的卡牌游戏，alice和bob分别持有若干1卡牌和2卡牌，和若干公共的0卡牌
游戏规则是抽取自己面前面值的卡牌（数量减1）或者0卡牌（数量减1并且翻转alice和bob分别持有的卡牌）
其中先手alice预先指定bob的卡牌面值并且减少一张该面值的卡牌数量
游戏的目的是
1。直到某方没有卡牌可抽，另一方仍然有牌，有牌的一方赢
2。双方都没有卡牌了，那么alice输掉比赛

思考的过程如下：
a 如果只有0卡牌，alice必输，因为游戏可以进行到双方都没有卡牌；
b 如果没有0卡牌，alice和bob将轮回抽取自己面前的卡牌，那么alice要想取胜，显然alice需要选择更多的卡牌数量，作为先手的alice可以将数量较少的卡牌安排给bob，如果1和2的数量一样，任意选择即可，因为alice可以将该卡牌数量减1。注意到alice要使用该必胜招数的条件是最少1或者2不能为0，否则较大堆必定落到bob手中，bob必胜
c 偶数数量的0卡牌类似b，因为无论哪一方使用里0卡牌来翻转，另一方都可以同样使用0卡牌来抵消对方的操作，所以等于没有0卡牌
d 奇数数量的0卡牌，相当于双方拥有的卡牌将会翻转一次，这时alice要想必胜就不能给bob选择数量少的卡牌，而是数量更多的
我们来看bob的策略
i如果bob卡牌数量少，那么立马用0卡牌翻转一次，这样alice必输
ii如果bob和alice卡牌数量一样，同样立马用0卡牌翻转一次，这样游戏可以一直进行到最后，那么alice输
iii如果bob比alice卡牌数量多一个，bob用掉该卡牌，两者卡牌一样多，可以保证游戏进行到最后，那么alice输
iiii如果bob比alice卡牌数量多两个以上，bob以上两种策略将失效，alice总是可以夺回卡牌较多的那一堆
class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cc = [0]*3
        for s in stones:
            cc[s%3] += 1
        if cc[0]%2 == 0:
            return cc[1] > 0 and cc[2] > 0
        return cc[1] > cc[2] + 2 or cc[2] > cc[1] + 2






# 由于我们只关心总和能否被 333 整除，我们可以将 stones[i]\textit{stones}[i]stones[i] 按照模 333 的结果分为 333 组，即 000、111 和 222。

# 根据题意，第一回合不能移除 000，否则直接输掉游戏，因此第一回合只能移除 111 或者 222。我们可以枚举这两种情况，如果其中一种可以让 Alice 获胜就返回 true\texttt{true}true，否则返回 false\texttt{false}false。

# 下面以第一回合移除 111 来说明。在不考虑移除 000 的前提下，后面的移除由于要满足总和不能被 333 整除，因此移除的石子是固定的，整体构成一个 112121212…112121212\dots112121212… 循环的序列。

# 对于 000，由于移除之后不会改变总和模 333 的结果，因此不会改变后续 111 和 222 的移除顺序，所以我们可以在序列的任意非开头位置插入 000。

# 两人为了不让自己输掉，必然会按照上述序列进行，直到没有石子，或某一方只能移除导致总和被 333 整除的石子时分出胜负。因此我们要求的就是让总和不能被 333 整除的最大的回合数，这相当于 112121212…112121212\dots112121212… 序列的最长长度，加上 000 的个数。

# 若该回合数为奇数，且还有剩余石子，那么下一回合要轮到 Bob 移除石子，且他只能移除一枚让总和被 333 整除的石子，于是 Alice 获胜；否则 Bob 获胜。

# 对于第一回合移除 222 的情况，同样会构成一个 221212121…221212121\dots221212121… 循环的序列，做法同上。

# 作者：endlesscheng
# 链接：https://leetcode-cn.com/problems/stone-game-ix/solution/guan-jian-zai-yu-qiu-chu-hui-he-shu-by-e-mcgv/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = [0]*3
        for st in stones:
            cnt[st%3] += 1
            
        def check(s):
            if cnt[0]%2 == 0:
                return cnt[s] > 0 and cnt[3-s] > cnt[s]-1
            return cnt[s]-2 > cnt[3-s]
        return check(1) or check(2)




class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        def check(i, cnt):
            if cnt[i] == 0:
                return False
            cnt[i] -= 1
            s = i 
            while cnt[s]:
                cnt[s] -= 1
                s = 3-s
            if cnt[1] == cnt[2] == 0:
                return False
            if cnt[0]%2 == 1:
                s = 3-s
            return s == i 
        cc = Counter([s%3 for s in stones])
        return check(1, cc.copy()) or check(2, cc.copy())
