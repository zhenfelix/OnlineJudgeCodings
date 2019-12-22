"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(cur, visited):
            cpy = Node(cur.val,[])
            visited[cur] = cpy
            cpy.neighbors = [dfs(neighbor, visited) if neighbor not in visited else visited[neighbor] for neighbor in cur.neighbors]
            return cpy

        return dfs(node, {})

