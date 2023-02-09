class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split()
        n = len(sentence)
        return all(sentence[i][0] == sentence[i-1][-1] for i in range(n))