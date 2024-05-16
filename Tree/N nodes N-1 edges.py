from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def build_tree(n, edges):
    if n == 0:
        return None
    
    # Step 1: Build the adjacency list
    adjacency_list = defaultdict(list)
    for u, v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
    
    # Step 2: Initialize nodes
    nodes = {i: TreeNode(i) for i in range(n)}

    # Step 3: Build the tree using BFS
    def bfs_build_tree(root):
        visited = [False] * n
        queue = deque([root])
        visited[root.val] = True

        while queue:
            node = queue.popleft()
            for neighbor in adjacency_list[node.val]:
                if not visited[neighbor]:
                    child_node = nodes[neighbor]
                    node.add_child(child_node)
                    visited[neighbor] = True
                    queue.append(child_node)
    
    # Choose node 0 as the root
    root = nodes[0]
    bfs_build_tree(root)
    
    return root


n = 5
edges = [
    (0, 1),
    (0, 2),
    (1, 3),
    (1, 4)
]

root = build_tree(n, edges)

def print_tree(node, level=0):
    if node:
        print("  " * level + str(node.val))
        for child in node.children:
            print_tree(child, level + 1)

print_tree(root)
