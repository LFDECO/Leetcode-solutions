"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        queue=deque()
        if not node:
            return None
        map1={}
        map1[node]=Node(node.val)
        queue.append(node)
        while queue:
            new_n=queue.popleft()
            for nei in new_n.neighbors:
                if nei not in map1:
                    map1[nei]=Node(nei.val)
                    queue.append(nei)
                map1[new_n].neighbors.append(map1[nei])

            
        return map1[node]