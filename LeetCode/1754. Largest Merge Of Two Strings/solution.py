字符串后缀排序+证明
首先说做法。每次比较word1和word2，将其中字典序较大的字符串的头部元素删除追加到我们的merge中即可。这个过程，可以直接通过暴力比较O(nm)O(nm)O(nm)，或者一些复杂的后缀处理技术，比如后缀数组来提速，时间复杂度为O(n+m)O(n+m)O(n+m)。

下面说明一下这样做为什么是对的。证明方法比较复杂，如果有更简洁的证明方法，欢迎在评论区提出。

首先我们可以在两个字符串尾部都加上一个代表无穷小的哨兵字符#，这样就可以避免讨论两个字符串一者是另外一者的前缀这种情况（但是两个字符串还是可能相同的）。很显然最后构建的字符串的尾部两个元素就是我们加入的哨兵字符。

接下来，我们简单用AAA表示word1，AiA_iAi​表示word1的第iii个字符，同理用BBB表示word2。记inv(Ai)inv(A_i)inv(Ai​)表示AiA_iAi​在最终结果（merge）中的下标。

如果A=BA=BA=B，很显然从哪个字符串头部删除都不会影响结果。下面认为A>BA\gt BA>B。我们记ttt为第一个不同的位置，即A1=B1,…,At−1=Bt−1A_1=B_1,\ldots,A_{t-1}=B_{t-1}A1​=B1​,…,At−1​=Bt−1​，但是At>BtA_t\gt B_tAt​>Bt​。

首先我们证明如果最终结果最优，则AtA_tAt​一定出现在BtB_tBt​之前。如果不是，记L=inv(Bt)L=inv(B_t)L=inv(Bt​)，此时BtB_tBt​在前。则对于所有1≤i≤t1\leq i\leq t1≤i≤t，我们将最终结果中AiA_iAi​与BiB_iBi​位置互换。此时可能发现换位后BiB_iBi​出现在Bt+1B_{t+1}Bt+1​之后的情况，我们可以将所有BBB占据的位置上的元素按照它们的下标重新排个序即可。可以发现修改后merge的长度为L−1L-1L−1的前缀是不会改变的，而第LLL个元素从BtB_tBt​变成了AtA_tAt​，增大了，这说明了我们最终结果并不是最优的，与前提相悖。因此inv(At)<inv(Bt)inv(A_t)\lt inv(B_t)inv(At​)<inv(Bt​)。

之后我们证明至少存在一种最优结果，满足inv(A1)=1inv(A_1)=1inv(A1​)=1，即AAA头部元素放在merge的最前。证明方法也是构造性的，从任意一个最优解出发，如果此时最优解的头部元素是B1B_1B1​而不是A1A_1A1​，我们记jjj表示最大的下标，满足inv(Bj)<inv(At)inv(B_j)\lt inv(A_t)inv(Bj​)<inv(At​)。之后我们将A1A_1A1​与B1B_1B1​的位置互换。可以发现我们的最优解值是不会变的。但是这时候可能出现冲突，即inv(B1)>inv(B2)inv(B_1)\gt inv(B_2)inv(B1​)>inv(B2​)，B1B_1B1​被交换到B2B_2B2​之后了。我们可以继续让B2B_2B2​与A2A_2A2​交换位置。重复上面这个流程直到结束。很显然这个流程是会结束的，因为BjB_jBj​不管是否交换都不会出现在Bj+1B_{j+1}Bj+1​之后。而这个过程由于不会改变解的值，因此修改后的解依旧最优，且此时inv(A1)=1inv(A_1)=1inv(A1​)=1。

因此根据上面的结果就可以放心大胆的使用贪心算法，因为无论如何都可以通过后续的手段将结果最优化。

作者：tian-tang-6
链接：https://leetcode-cn.com/problems/largest-merge-of-two-strings/solution/zi-fu-chuan-hou-zhui-pai-xu-zheng-ming-b-hen2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


补充一下步骤二中的最后一步，看了好久才理清。在Ai和Bi交换之后可能会出现两种类型的冲突，1。inv(B_i+1) < inv(A_i) 或者2。inv(A_i+1) < inv(B_i)。首先注意到不会同时存在冲突1和2，否则联立这两个不等式和 inv(A_i) < inv(A_i+1) 得到矛盾 inv(B_i+1) < inv(B_i)。接下来注意到初始条件inv(B_1)=1所以初始情况下如果出现冲突，那么一定是冲突1。那么当冲突1结束的时候会不会出现冲突2呢，答案是不会。假如当前出现冲突2。inv(A_i+1) < inv(B_i)，并且在上一个状态出现冲突1。inv(B_i) < inv(A_i-1)，联立这两个不等式和inv(A_i-1) < inv(A_i+1)，可以推出矛盾inv(B_i) < inv(B_i)。所以冲突1结束的时候就是不存在冲突了，由于inv(B_j+1) > inv(A_t) > inv(A_j)，所以冲突1是必然会结束的


class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        word1 = list(word1)
        word2 = list(word2)
        return ''.join([max(word1,word2).pop(0) for _ in word1+word2])



class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        res = []
        while word1 and word2:
            if word1 >= word2:
                res.append(word1[0])
                word1 = word1[1:]
            else:
                res.append(word2[0])
                word2 = word2[1:]
        res = ''.join(res)
        if word1:
            res = res + word1
        else:
            res = res + word2
        return res 