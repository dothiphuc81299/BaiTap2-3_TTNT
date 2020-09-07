import networkx as nx

G = nx.Graph()
G.add_nodes_from(["S", "A", "B", "C", "D", "E", "F", "G", "H"])
G.add_weighted_edges_from(
    [
        ("S", "A", 3),
        ("S", "B", 6),
        ("A", "D", 3),
        ("S", "C", 2),
        ("B", "G", 9),
        ("B", "E", 2),
        ("C", "E", 1),
        ("D", "F", 5),
        ("E", "H", 5),
        ("F", "E", 6),
        ("H", "G", 8),
        ("F", "G", 5),
    ]
)

class node_cost:
    def __init__(self, node, cost):
        self.node = node
        self.cost = cost

def print_node(array):
    for i in array:
        print("("+i.node + ","+ str(i.cost)+") " ,end = '')
    print()

def min_node_cost(frontier):
    minn = min(e.cost for e in frontier)
    for i in frontier:
        if(i.cost == minn):
            return i

def get_label(frontier):
    result = []
    for i in frontier:
        result.append(i.node)
    return result

def uniform_cost_search(graph, initial_state, goalTest):
    global state
    frontier = []
    frontier.append(node_cost(initial_state, 0))
    explored = []
    while len(frontier) > 0:
        print_node(frontier)
        # print_node(explored)
        # print("---")
        state = min_node_cost(frontier)
        explored.append(state)
        if(state.node == goalTest):
            return True
        frontier.remove(state)
        for neighbor in G.neighbors(state.node):
            explored_node = get_label(explored)
            frontier_node = get_label(frontier)

            if neighbor not in explored_node:
                if neighbor not in frontier_node:
                    frontier.append(node_cost(neighbor, state.cost+G.get_edge_data(state.node, neighbor)["weight"]))
                elif neighbor in frontier_node :
                    for i in frontier:
                        temp_cost = state.cost+G.get_edge_data(state.node, neighbor)["weight"]
                        if i.node==neighbor and (temp_cost<=i.cost):
                            i.cost = temp_cost

    return False

if __name__ == '__main__':
    print(uniform_cost_search(G, "S", "G"))

    # state = "S"
    # frontier = []
    # explorer = []
    # for neighbor in G.neighbors(state):
    #     # print(neighbor + str(G.get_edge_data("S", neighbor)["weight"]))
    #     frontier.append(node_cost(neighbor, G.get_edge_data("S", neighbor)["weight"]))
    # print_node(frontier)
    # temp = get_label(frontier)
    # print(temp)
    # minn = min_node_cost(frontier)
    # print(minn.node + " " + str(minn.cost))
    # frontier.remove(minn)
    # print_node(frontier)
    # if(minn.node == "C"):
    #     print(True)

    # minn = 0
    # for i in frontier:
    #     minn = min(e.cost for e in frontier)
    # print(minn)
    #
    # for i in frontier:
    #     if(i.cost == minn):
    #         frontier.remove(i)
    #         explorer.append(i)
    # print()
    # print_node(frontier)
    # print()
    # print_node(explorer)

    # print(G.number_of_nodes())
    # print(G.number_of_edges())
    #
    # mang = []
    # mang.append(node_cost('a', 2))
    # mang.append(node_cost('b', 3))
    # print_node(mang)
    # for i in mang:
    #     if(i.cost == 2):
    #         mang.remove(i)
    # print_node(mang)
    # # print()
    # # print(min(e.cost for e in mang))
    #
    # for neighbor in G.neighbors("S"):
    #     print(neighbor)
        # print(str(G.get_edge_data("S", neighbor)["weight"]))
    # uniform_cost_search(G,"S","G")