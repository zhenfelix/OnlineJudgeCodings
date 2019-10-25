from collections import deque

class Solution:
    def crawl(self, startUrl, htmlParser) -> List[str]:
        q = deque()
        visited = set()
        q.append(startUrl)  
        visited.add(startUrl)      
        hostname = startUrl.split("://")[1].split("/")[0]
        ans = []
        while q:
            cur = q.popleft()
            if hostname not in cur:
                continue
            ans.append(cur)
            for url in htmlParser.getUrls(cur):
                if url not in visited:
                    visited.add(url)
                    q.append(url)
        return ans