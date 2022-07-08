class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        res = []
        def check(ws):
            return ws[0] == '$' and len(ws) > 1 and all(w.isdigit() for w in ws[1:])
        for word in sentence.split():
            if check(word):
                price = int(word[1:])
                price *= (100-discount)/100
                price = '{:.2f}'.format(round(price, 2))
                
                res.append('$'+price)
            else:
                res.append(word)
        return ' '.join(res)



class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        lst = sentence.split(' ')
        ans = []
        for s in lst:
            t = s
            if s.startswith('$') and len(s) > 1:
                for i in range(1, len(s)):
                    if ord(s[i]) < ord('0') or ord(s[i]) > ord('9'):
                        break
                else:
                    t = '$' + ('%.2f' % (int(s[1:]) * (1 - discount / 100)))
            ans.append(t)
        return ' '.join(ans)


作者：TsReaper
链接：https://leetcode.cn/circle/discuss/E0MOm0/view/YyNtoI/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。