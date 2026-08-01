"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        hash_map = {}
        def traverse(node):
            hash_map[node.val] = [nd.val for nd in node.neighbors]
            for neighbor in node.neighbors:
                if neighbor.val not in hash_map.keys():
                    traverse(neighbor)
        
        traverse(node)

        new_node_map = {}
        for item in hash_map.keys():
            new_node_map[item] = Node(item)
        for val,node in new_node_map.items():
            for nb in hash_map[val]:
                node.neighbors.append(new_node_map[nb])
        

        return new_node_map[1]
          
        