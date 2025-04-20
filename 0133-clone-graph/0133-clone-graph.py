"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = {}
        q = deque()
        q.append(node)

        visited[node] = Node(node.val)
        while q:
            now = q.popleft()

            for next in now.neighbors:
                if next not in visited:
                    visited[next] = Node(next.val)
                    q.append(next)
                
                visited[now].neighbors.append(visited[next])
        
        return visited[node]