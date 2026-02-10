import collections as c


graph = {
    "A": ["B"],
    "B": ["C", "D"],
    "C": ["E"],
    "D": ["F"],
    "E": [],
    "F":[]
}

visited = set() 


def bfs(node, graph, visited, dNode):
    queue = c.deque()

    queue.append(node)

    while queue:
        newNode = queue.popleft()

        visited.add(newNode)
        
        print(newNode)

        if newNode == dNode:
            break

        for neighbor in graph[newNode]:
            queue.append(neighbor)


print("this is Breadth-First Search (BFS) for question 1a ")
bfs("A", graph, visited, "E")