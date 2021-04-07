# Implementation of the iterative deeping
# algorithm for finding a route between cities.

from data import init_routes, create_child_node_list


def dfs(target, node, data, depth, threshold, seen_nodes=[]):
    seen_nodes.append(node)
    if node == target:
        return True

    new_nodes = create_child_node_list([node], data)
    new_nodes = list(new_nodes - set(seen_nodes))
    print("Layer:", new_nodes)

    while new_nodes or depth < threshold:
        result = dfs(target, new_nodes[0], data, depth + 1, threshold, seen_nodes)
        if result:
            return True
        new_nodes = new_nodes[1:]

    return False


def iterative_deeping(target, node, data):
    threshold = 0
    result = False
    while not result:
        result = dfs(target, node, data, 0, threshold)
        threshold += 1
        print("Depth:", threshold)

    print("Solution found!")


if __name__ == "__main__":
    # Get the test data.
    routes = init_routes()

    # The city you want to start and end at.
    start = "Linz"
    target = "Ulm"

    # Search for the solution.
    iterative_deeping(target, start, routes)

