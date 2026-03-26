# Depth First Search (DFS)

## Overview
Depth First Search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.

## How it Works
1. Start by putting any one of the graph's vertices on top of a stack (or use recursion which acts as an implicit stack).
2. Take the top item of the stack and add it to the visited list.
3. Create a list of that vertex's adjacent nodes. Add the ones which aren't in the visited list to the top of the stack.
4. Keep repeating steps 2 and 3 until the stack is empty.

## Complexity
- **Time Complexity:** $O(V + E)$, where $V$ is the number of vertices and $E$ is the number of edges. This is because every vertex and every edge will be explored in the worst case.
- **Space Complexity:** $O(V)$, where $V$ is the number of vertices. This space is required for the visited array/set and the recursion stack.

## Applications
- Finding connected components in a graph.
- Topological sorting.
- Finding paths between two nodes.
- Solving puzzles like mazes.
- Detecting cycles in a graph.

## Implementation Details
The provided `dfs.py` contains a straightforward recursive approach using a Python dictionary to represent the graph as an adjacency list.
