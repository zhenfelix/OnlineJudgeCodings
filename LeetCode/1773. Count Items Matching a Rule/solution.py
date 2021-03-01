class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        return sum(1 for t, c, n in items if (ruleKey, ruleValue) in (("type", t), ("color", c), ("name", n)))


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        mp = {'type': 0, 'color': 1, 'name': 2}
        cnt = 0
        for i, v in enumerate(items):
            if v[mp[ruleKey]] == ruleValue:
                cnt += 1
        return cnt