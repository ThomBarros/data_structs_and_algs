from queue import DynamicArrayQueue

def bfs_queue(graph, root, visited=None):
    if visited is None:
        visited = []

    queue = DynamicArrayQueue()
    queue.enqueue(root)

    while not queue.empty():
        v = queue.dequeue()

        if v not in visited:
            visited.append(v)

        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                queue.enqueue(w)

    return visited


def run_tests():
    graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}
    print(graph)
    found_nodes = bfs_queue(graph, "A")
    print(found_nodes)


if __name__=="__main__":
    run_tests()

