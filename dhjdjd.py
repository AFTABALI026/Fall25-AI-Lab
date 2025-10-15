graph = {
    'P': ['Q', 'R'],
    'Q': ['S', 'T'],
    'R': ['U'],
    'S': ['V', 'W'],
    'T': [],
    'U': ['X', 'Y'],
    'V': [],
    'W': ['Z'],
    'X': [],
    'Y': ['AA'],
    'Z': [],
    'AA': []
}

def depth_first_search(start, goal):
    if start not in graph or goal not in graph:
        print("Start or goal not found in graph!")
        return None
    
    stack = [(start, [start])]
    
    while stack:
        node, path = stack.pop()
        print("Checking:", node)

        if node == goal:
            return path

        for adj in reversed(graph[node]):
            if adj not in path:
                stack.append((adj, path + [adj]))


print(depth_first_search("P", "Z"))
