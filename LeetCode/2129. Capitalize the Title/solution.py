class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        for i, w in enumerate(words):
            words[i] = w.lower()
            if len(w) >= 3:
                words[i] = words[i][0].upper()+words[i][1:]
        return ' '.join(words)