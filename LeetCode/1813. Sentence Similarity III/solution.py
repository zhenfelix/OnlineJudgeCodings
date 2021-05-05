class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        w1, w2 = s1.split(" "), s2.split(" ")
        if len(w1) < len(w2):
            w1, w2 = w2, w1
        i, j, dif = 0, len(w2) - 1, len(w1) - len(w2)
        while i < len(w2) and w2[i] == w1[i]:
            i += 1
        while j >= 0 and w2[j] == w1[j + dif]:
            j -= 1
        return i > j        