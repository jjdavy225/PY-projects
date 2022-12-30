def color_graph(matrix, num_colors):
    # Create a dictionary to store the colors of each vertex
    colors = {}
    
    # Get the list of vertices in the graph
    vertices = list(range(len(matrix)))
    # print(vertices)
    
    # Sort the vertices by degree (number of edges)
    sorted_vertices = sorted(vertices, key = lambda x: sum(matrix[x]), reverse = True)
    # print(sorted_vertices)
    
    # Iterate over the vertices in order of decreasing degree
    for vertex in sorted_vertices:
        # Create a set of available colors
        available_colors = set(range(num_colors))
        print(vertex)
        # print(available_colors)
        
        # Remove any colors that are already used by adjacent vertices
        for neighbor in range(len(matrix)):
            # print(neighbor)
            print(range(len(matrix)))
            if matrix[vertex][neighbor] == 1 and neighbor in colors:
                available_colors.remove(colors[neighbor])
                # print(available_colors)
        
        # Assign the first available color to the vertex
        colors[vertex] = min(available_colors)
    
    return colors

# Example usage

# Create a graph represented as an adjacency matrix
matrix = [
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0]
]

# Color the graph using 3 colors
colors = color_graph(matrix, 3)

# Print the resulting coloring
print(colors)
