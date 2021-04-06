# This file contains some example data
# to test the different search algorithms.

from dataclasses import dataclass

@dataclass(frozen=True)
class Route:
    """Class for keeping track of routes."""
    id: int
    city_start: str
    city_end: str
    distance: int


def create_child_node_list(start_nodes, data):
    """Determines the child of every node."""
    node_list = []
    for node in start_nodes:
        for route in data:
            if route.city_start == node:
                node_list.append(route.city_end)

            if route.city_end == node:
                node_list.append(route.city_start)

    return set(node_list)
    

def init_routes():
    routes = []
    routes.append(Route(1, "Frankfurt", "Würzburg", 111))
    routes.append(Route(2, "Würzburg", "Nürnberg", 104))
    routes.append(Route(3, "Nürnberg", "Bayreuth", 75))
    routes.append(Route(4, "Nürnberg", "Mannheim", 230))
    routes.append(Route(5, "Frankfurt", "Mannheim", 85))
    routes.append(Route(6, "Karlsruhe", "Mannheim", 67))
    routes.append(Route(7, "Karlsruhe", "Stuttgart", 64))
    routes.append(Route(8, "Würzburg", "Stuttgart", 140))
    routes.append(Route(9, "Würzburg", "Ulm", 183))
    routes.append(Route(10, "Stuttgart", "Ulm", 107))
    routes.append(Route(11, "Nürnberg", "Ulm", 171))
    routes.append(Route(12, "München", "Ulm", 123))
    routes.append(Route(13, "München", "Nürnberg", 170))
    routes.append(Route(14, "Passau", "Nürnberg", 220))
    routes.append(Route(15, "Passau", "München", 189))
    routes.append(Route(16, "Passau", "Linz", 102))
    routes.append(Route(17, "Salzburg", "Linz", 126))
    routes.append(Route(18, "Salzburg", "Rosenheim", 81))
    routes.append(Route(19, "München", "Rosenheim", 59))
    routes.append(Route(20, "Innsbruck", "Rosenheim", 93))
    routes.append(Route(21, "Innsbruck", "Landeck", 73))
    routes.append(Route(22, "Memmingen", "München", 115))
    routes.append(Route(23, "Memmingen", "Ulm", 55))
    routes.append(Route(24, "Memmingen", "Zürich", 184))
    routes.append(Route(25, "Bern", "Zürich", 120))
    routes.append(Route(26, "Bern", "Basel", 91))
    routes.append(Route(27, "Zürich", "Basel", 85))
    routes.append(Route(27, "Karlsruhe", "Basel", 191))
    return routes

