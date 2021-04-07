# Implementation of the
# - Breadth-First Search (BFS) algorithm
# - Depth-first search (DFS) algorithm
# for finding a route between cities.

from data import init_routes, create_child_node_list


def bfs(target, node_list, data):
    for node in node_list:
        if node == target:
            print("Solution found.")
            return
    new_nodes = create_child_node_list(node_list, data)
    print("Layer:", new_nodes)

    if new_nodes:
        bfs(target, new_nodes, data)
    else:
        print("There is no solution.")


def dfs(target, node, data, seen_nodes=[]):
    seen_nodes.append(node)
    if node == target:
        print("Solution found.")
        return True

    new_nodes = create_child_node_list([node], data)
    new_nodes = list(new_nodes - set(seen_nodes))
    print("Layer:", new_nodes)

    while new_nodes:
        result = dfs(target, new_nodes[0], data, seen_nodes)
        if result:
            print("Solution found.")
            return True
        new_nodes = new_nodes[1:]

    print("There is no solution.")
    return False


if __name__ == "__main__":
    # Get the test data.
    routes = init_routes()

    # The city you want to start and end at.
    start = "Linz"
    target = "Ulm"

    bfs(target, [start], routes)
    dfs(target, start, routes)
