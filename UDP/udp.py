class Node:
    def __init__(self, name):
        self.name = name
        self.routing_table = {}  # {destination: (next_hop, cost)}

    def update_routing_table(self, destination, next_hop, cost):
        if destination not in self.routing_table or cost < self.routing_table[destination][1]:
            self.routing_table[destination] = (next_hop, cost)

class Network:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.name] = node

    def update_distance_vector_routing(self, source, destination, cost):
        for node_name, node in self.nodes.items():
            if node_name != source:
                if node_name != destination:
                    if destination in node.routing_table:
                        existing_cost = node.routing_table[destination][1]
                        if source not in node.routing_table or cost + existing_cost < node.routing_table[source][1]:
                            node.update_routing_table(source, source, cost + existing_cost)
                    else:
                        if source not in node.routing_table:
                            node.update_routing_table(source, source, cost)

    def print_routing_tables(self):
        for node_name, node in self.nodes.items():
            print(f"Routing table for {node_name}:")
            print("Destination\tNext Hop\tCost")
            for destination, (next_hop, cost) in node.routing_table.items():
                print(f"{destination}\t\t{next_hop}\t\t{cost}")
            print("\n")

def main():
    A = Node('A')
    B = Node('B')
    C = Node('C')
    D = Node('D')

    network = Network()
    network.add_node(A)
    network.add_node(B)
    network.add_node(C)
    network.add_node(D)

    A.update_routing_table('A', 'A', 0)
    B.update_routing_table('B', 'B', 0)
    C.update_routing_table('C', 'C', 0)
    D.update_routing_table('D', 'D', 0)

    network.update_distance_vector_routing('A', 'B', 1)
    network.update_distance_vector_routing('A', 'C', 2)
    network.update_distance_vector_routing('B', 'C', 3)
    network.update_distance_vector_routing('C', 'D', 1)

    network.print_routing_tables()

if __name__ == "__main__":
    main()
