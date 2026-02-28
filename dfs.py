from dynamic_array import DynamicArray


def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = [] 
    
    visited.append(vertex)

    for neighbour in graph[vertex]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)

    return visited
    

def dfs_stack(graph, vertex, visited=None):
    visited = []
    stack = DynamicArray()
    stack.push(vertex) 

    while not stack.isEmpty():
        curr_vertex = stack.pop()

        if curr_vertex not in visited:
            visited.append(curr_vertex)
            neighbour = graph[curr_vertex]

            for i in range(len(neighbour) - 1, -1, -1):
                if neighbour[i] not in visited:
                    stack.push(neighbour[i]) 

    return visited



def run_tests():
    graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}
    print(graph)
    found_nodes = dfs(graph, "A")
    print(found_nodes)
    graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}
    print(graph)
    found_nodes = dfs_stack(graph, "A")
    print(found_nodes)




if __name__=="__main__":
    run_tests()

