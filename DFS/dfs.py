def dfs(graph, start, visited=None):
    """
    Depth First Search (DFS) traversal of a graph.
    
    Args:
        graph: A dictionary representing an adjacency list.
               Keys are nodes and values are sets of connected nodes.
        start: The starting node for the traversal.
        visited: A set to keep track of visited nodes.
    """
    if visited is None:
        visited = set()
    visited.add(start)

    print(start, end=" ")

    # Recursively visit all unvisited neighbors
    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited)
    
    return visited

if __name__ == '__main__':
    # Example graph represented as an adjacency list
    # 0 --- 1 --- 3
    # |     |
    # 2 --- 4
    sample_graph = {
        '0': set(['1', '2']),
        '1': set(['0', '3', '4']),
        '2': set(['0', '4']),
        '3': set(['1']),
        '4': set(['1', '2'])
    }

    print("Depth First Search Traversal starting from node '0':")
    dfs(sample_graph, '0')
    print() # For newline
