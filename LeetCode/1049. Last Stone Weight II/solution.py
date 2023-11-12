class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        tot = sum(stones)
        target = tot//2
        dp = [0]*(target+1)
        dp[0] = 1
        for x in stones:
            for t in range(target, x-1, -1):
                dp[t] |= dp[t-x]
        for t in range(target,-1,-1):
            if dp[t]:
                return tot-t-t
        return -1


# 前言：合法性证明

# 为了便于讨论，若最终没有石头剩下，则视作最终剩下了一块重量为 000 的石头。

# 用归纳法可以证明，无论按照何种顺序粉碎石头，最后一块石头的重量总是可以表示成
# ∑i=0n−1ki×stonesi,  ki∈{−1,1}\sum_{i=0}^{n-1} k_i \times \textit{stones}_i,\ \ k_i\in\{-1,1\}i=0∑n−1​ki​×stonesi​,  ki​∈{−1,1}

# 但不是所有 kik_iki​ 的取值都是合法的。例如有四块石头，其重量分别为 aaa，bbb，ccc，ddd，且满足 a≤b≤c≤da\le b\le c\le da≤b≤c≤d。由于石头的重量不可能增加，无论怎么操作，我们是不可能得到大小为 d+c+b−ad+c+b-ad+c+b−a 的石头的，该重量已经超过了 ccc 以及 ddd。

# 那么，上述和式的最小非负值所对应的这组 {ki}\{k_i\}{ki​} 是合法的吗？

# 我们将这组 {ki}\{k_i\}{ki​} 对应的石头划分成两堆，ki=1k_i=1ki​=1 的石头分至一堆，ki=−1k_i=-1ki​=−1 的石头分至另一堆。由于这是最小非负值所对应的 {ki}\{k_i\}{ki​}，这两堆石头重量之差的绝对值也是所有划分当中最小的。

# 记这两堆石头重量之差的绝对值为 diff\textit{diff}diff。若能找到一种粉碎方案，使得最后一块石头的重量也为 diff\textit{diff}diff，那就能说明这组 {ki}\{k_i\}{ki​} 是合法的。

# 我们不断地粉碎石头。每次粉碎时，记重量最大的石头所处的堆为 AAA（若两堆最大重量相同则任选一堆），另一堆为 BBB。从 AAA 中取出重量最大的石头，BBB 中任取一石头，若没有完全粉碎，则将新石头重新放入 AAA。这一操作从每堆石头中减去了同样的重量，从而保证重量之差的绝对值在粉碎前后是不变的。

# 若出现一堆没有石头，而另一堆不止一块石头的情况，记有石头的那一堆为 AAA，另一堆为 BBB。要继续粉碎，则需要从 AAA 中取出一块石头移入 BBB，然后按规则粉碎。但移入操作让重量之差的绝对值变得更小，与事实（上文加粗文字）矛盾，所以不会出现这种情况。

# 因此，按照上述流程操作，最后一块石头的重量为 diff\textit{diff}diff，所以这组 {ki}\{k_i\}{ki​} 对应着一个合法的粉碎结果。

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/last-stone-weight-ii/solutions/817930/zui-hou-yi-kuai-shi-tou-de-zhong-liang-i-95p9/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。