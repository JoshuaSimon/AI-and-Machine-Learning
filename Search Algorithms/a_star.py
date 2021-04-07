# Implementation of the A*-Algorithm 
# for finding a route between cities.

from data import init_routes, init_beeline, create_ordered_child_node_list


def a_star(start_node, target_node, data, heuristic):
    node_list = [start_node]
    seen_nodes = []
    counter = 0

    while True:
        if not node_list:
            print("There is no solution.")
            return True

        node = node_list[0]
        node_list = node_list[1:]
        seen_nodes.append(node)
        print("Step:", counter, "Node:", node)

        if node == target_node:
            print("Solution found!")
            return True

        node_list = create_ordered_child_node_list(node, data, heuristic)
        node_list = list(node_list - set(seen_nodes))
        print("Node List:", node_list)
        counter += 1




if __name__ == "__main__":
# Get the test data.
    routes = init_routes()
    beelines = init_beeline()

    # The city you want to start and end at.
    start = "Frankfurt"
    target = "Ulm"

    a_star(start, target, routes, beelines)
