import math

A = 'A'
B = 'B'
C = 'C'
D = 'D'
E = 'E'
F = 'F'
G = 'G'
H = 'H'

adj_list = {
  A: {B:1, C:2},
  B: {A:1, E:4},
  C: {A:2, D:1, F:3},
  D: {C:1, E:1},
  E: {B:4, D:1, G:2},
  F: {C:3, G:2},
  G: {E:2, F:2, H:4},
  H: {G:4}
}

queue = [A]
visited = [A]
dist = {n:math.inf for n in adj_list}

predecessor = {n:None for n in adj_list}

dist[A] = 0

print(dist)

while queue:
  # This find the node with shortest distance
  # TODO: make it nice
  node = queue[0]

  for n in queue:
    if dist[n] < dist[node]:
      node = n

  queue.remove(node)

  for neighbour in adj_list[node]:
    new_dist = dist[node] + adj_list[node][neighbour]

    if new_dist < dist[neighbour]:
      dist[neighbour] = new_dist
      predecessor[neighbour] = node
    
    if neighbour not in visited:
      queue.append(neighbour)
      visited.append(neighbour)

print(visited)
print(dist)
print(predecessor)
cursor = 'H'

while cursor:
  print(cursor)
  cursor = predecessor[cursor]
