graph = {
    'A': ['B', 'C'],
    'B': ['C', 'E'],
    'C': ['D'],
    'D': ['A'],
    'E': ['F'],
    'F': []
}

def transpose(graph):
    graphT = {node: [] for node in graph}  # Initialize all nodes in the graph with an empty list
    for node in graph:
        for neighbor in graph[node]:
            if node not in graph[neighbor]: # Case where some edges are bidirectional
                graphT[neighbor].append(node)

    return graphT

print(transpose(graph))


# Time Complexity: O(|E|) where |E| is the number of edges in the graph
# Space Complexity: O(|V| + |E|) where |V| is the number of vertices in the graphX  
