class Solution:
    def deleteText(self, article: str, index: int) -> str:
        if article[index] == ' ':
            return article
        cnt = 0
        words = article.split()
        for i, ch in enumerate(article):
            if ch == ' ':
                cnt += 1
            if i == index:
                return ' '.join(words[:cnt]+words[cnt+1:])
        return ''