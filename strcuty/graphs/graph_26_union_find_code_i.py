# Union Find Code I - Graph Problem
# Implementing union find data structure part 1

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function, count_components, that takes in a number of nodes (n) and a list of edges for an undirected graph. In the graph, nodes are labeled from 0 to n - 1. 
The function should return the number of connected components in the given graph.

EXAMPLES:
================================================================================
count_components(7, [
  (0, 2),
  (1, 0),
  (4, 3),
  (2, 5),
  (3, 6)
]) # -> 2
count_components(100, [
  (50, 60),
  (80, 20)
]) # -> 98


COMPLEXITY:
================================================================================

Memory Palace:
================================================================================

Story: Angry Birds Union Find

At the beginning there are Angry Birds hitting themselves into the ground and because of that they are jumping into the air. None of them land near each other, so every bird starts completely alone.

Then the birds are assigned to groups to attack different piggy bosses. The Angry Birds government is very secretive and it only tells you which two birds appear in front of each other. 
The government gives information pair by pair. For each pair it identifies which bird is at the front of the pair and whispers the target piggy boss to that front bird. 
The government always whispers the same target to all birds that truly belong to the same group, although the birds do not know this.

The government basically reveals the order in which birds stand on the caterpillars. It never reveals the full chain and it never declares who the true leaders are.

The birds become angry because they do not know who their leader is. They decide to create their own system.

If a bird does not have any other bird standing in front of it yet, it assumes that it is the leader of its group for now. Only the leader knows the target piggy boss for that group.

If a bird has never been assigned by the government at all, it is a free citizen, it is its own boss, and it does not have a target yet.

Leadership is constantly updated. Whenever the government announces a pair of birds, those two birds immediately ask each other who their leader is. 
Each bird follows the chain of birds in front of it until it reaches a bird who does not have any birds in front of them. That bird is the actual leader and it is the one that holds the target.

Since the government ensures that both leaders belong to the same target group, these two leaders hold a meeting. 
After talking, one leader keeps leadership and the other leader accepts that leadership. This action unifies the two chains into a single group that shares the same target.

By the end, all the announcements have been processed and the system settles into a few strong groups of Angry Birds. Each group has exactly one leader and they are ready to attack their assigned piggy bosses.

Memory Palace: 

Scene 1: The Jumping Birds

All Angry Birds slam into the ground and bounce away from each other.
Each lands alone.
Each bird is its own boss and knows nothing about targets.

Scene 2: Government Whisper Pairs

The secretive Angry Birds government appears on a floating cloud.
It announces birds pair by pair.
For each pair it points to the bird in front and whispers the piggy target into that bird’s ear.
The government always whispers the same target to birds that truly belong to the same group, but the birds do not know this.

Scene 3: The Shifting Angry Birds Battle Lines

Whenever a pair is announced, the two birds flap their wings, puff up their feathers, and jump into a loose battle line.
They squawk at each other, asking who their leader is.
To find out, each bird looks to the bird standing directly in front of them.
That bird then looks to the bird in front of them, and this continues forward as needed.
The whole line wobbles and shifts with birds hopping, shuffling, and bumping as they check who is ahead of them.
Eventually they reach a bird who has no one in front of them.
That bird stands tall, puffs up the biggest, and is recognized as the leader who holds the target.
All the other birds in that group circle the leader and squawk at the leader.

Scene 4: The Leader Meeting

Since the government has ensured that both leaders share the same target, the two leaders hop forward to a central meeting rock.
One leader keeps leadership.
The other leader accepts this leadership.
Their two shifting battle lines now act as one unified group under a single leader.

Scene 5: The Caterpillar Reveal

After all pair announcements are processed, the shifting battle lines settle.
The hidden structure becomes visible.
The birds reshape themselves into long caterpillars that show the true chains.
Each caterpillar has one leader at the very front, and each caterpillar begins marching proudly toward its assigned piggy boss.


"""

# SOLUTION:
# ================================================================================
# Iterative with no path compression
def count_components(n, edges):
  graph = {i : i for i in range(n)}
  for a, b in edges:
    a, b  = find(graph, a), find(graph, b)
    union(graph, a, b)
  count = 0
  for node in graph:
    if graph[node] == node:
      count += 1
  return count

def union(graph, a, b):
  graph[a] = b
    

def find(graph, a):
  while graph[a] != a:
    a = graph[a]
  return a

# Recursive: Alvin's
def find(roots, node):
  if node == roots[node]:
    return node
  return find(roots, roots[node])

def union(roots, node_a, node_b):
  root_a = find(roots, node_a)
  root_b = find(roots, node_b)
  roots[root_b] = root_a
      
def count_components(n, edges):
  roots = [ i for i in range(0, n) ]
  
  for edge in edges:
    node_a, node_b = edge
    union(roots, node_a, node_b)

  count = 0
  for i in range(0, len(roots)):
    if i == roots[i]:
      count += 1
      
  return count

    

