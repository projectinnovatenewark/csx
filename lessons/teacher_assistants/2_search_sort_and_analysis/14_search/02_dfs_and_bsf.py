"""
Depth first search and breadth first search
"""

def dfs(graph, start_node, end_node):
  unvisited = []
  unvisited.append(start_node)
  explored = set()
  while unvisited is not empty:
    current_node = unvisited.pop()
    if current_node in explored:
      continue
    if current_node == end_node:
      return 'success!'
    
    for neighbor in graph[current_node]:
      unvisited.append(neighbor)
    explored.add(current_node)