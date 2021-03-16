"""Three Algorithms to determine Shortest Path between vertices"""

import heapq
import math

def calculate_distances(graph, start):
  distances = {vertex: math.inf for vertex in graph} # Create dictionary to hold shortest paths for each vertex.
  distances[start] = 0 # Set path from starting vertex to itself as zero.
  seen = set()

  pq = [(0, start)] # Initialize our heap queue with a tuple of the distance and the start vertex.
                    # Heap will automatically sort based off of the first item in the tuple.
  while len(pq) > 0:
    print(f"pq: {pq}")
    current_distance, current_vertex = heapq.heappop(pq)
    print(f"current_distance: {current_distance}, current_vertex: {current_vertex}")

    # Nodes can get added to the priority queue multiple times. We only
    # process vertices that are "unseen".
    if current_vertex in seen:
      continue

    for neighbor, weight in graph[current_vertex].items(): # Iterate over key/value pairs using .items(), such
      distance = current_distance + weight                 # that neighbor is the key and weight is the value.

      # Only consider new path if it's better than the current
      # shortest path from the start to that vertex.
      if distance < distances[neighbor]:
        distances[neighbor] = distance
        heapq.heappush(pq, (distance, neighbor))

    seen.add(current_vertex)
  return distances

example_graph = {
    'A': {'B': 6, 'D': 1},
    'B': {'A': 6, 'D': 2, 'C': 5, 'E': 2},
    'C': {'B': 5, 'E': 5},
    'D': {'A': 1, 'B': 2, 'E': 1},
    'E': {'D': 1, 'C': 5, 'B': 2},
}
print(calculate_distances(example_graph, 'A'))