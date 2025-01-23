## MySQL

- https://www.mysqltutorial.org/mysql-basics/mysql-except/

## Python DSA 

- https://realpython.com/python-data-structures/


## Graph 

- Minimum spanning tree. graph of N nodes need N-1 connections/edges for all nodes to be connected directly/indirectly
- DFS 
```
# Example: DFS on a graph using recursion

def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")  # Process the node
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()
print("DFS Traversal:")
dfs(graph, 'A', visited)

```
- BFS 

```
from collections import deque

# Example: BFS on a graph using a queue

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")  # Process the node

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("\nBFS Traversal:")
bfs(graph, 'A')

```