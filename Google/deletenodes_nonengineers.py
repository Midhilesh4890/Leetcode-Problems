from collections import deque

class Employee:
    def __init__(self, employeeId, isEngineer):
        self.employeeId = employeeId
        self.isEngineer = isEngineer
        self.reportees = []

    def __repr__(self):
        # For easier debugging and printing.
        return f"Employee({self.employeeId}, isEngineer={self.isEngineer})"

def filter_engineers_bfs(root):
    """
    Given the root of the organizational tree, return a new tree containing only
    engineer nodes, constructed using a BFS approach.
    Assumption: The root is always an engineer.
    """
    if not root:
        return None

    # Create the new root (engineer node) # root is always an Engineer
    new_root = Employee(root.employeeId, True)
    
    # Queue holds tuples: (original node, effective new parent to attach engineer nodes)
    queue = deque([(root, new_root)])
    
    while queue:
        orig_node, effective_parent = queue.popleft()
        for child in orig_node.reportees:
            if child.isEngineer:
                # If the child is an engineer, create a new node and attach it
                new_child = Employee(child.employeeId, True)
                effective_parent.reportees.append(new_child)
                # Enqueue the child with its own new node as effective parent.
                queue.append((child, new_child))
            else:
                # If the child is NOT an engineer, we do not create a node for it.
                # Instead, we keep the effective parent the same,
                # so that any engineer reportees under this non-engineer
                # will be attached directly to the nearest engineer above.
                queue.append((child, effective_parent))
    
    return new_root

# Example usage:
if __name__ == '__main__':
    # Build the original tree:
    #             E1
    #        ______|_______
    #       |       |      |
    #      E2      NE1     E3
    #       |        |
    #      E4       E5
    #
    # Where:
    # - E1, E2, E3, E4, and E5 are Engineers.
    # - NE1 is a Non-Engineer.

    # Create nodes:
    E1 = Employee(1, True)
    E2 = Employee(2, True)
    NE1 = Employee(101, False)
    E3 = Employee(3, True)
    E4 = Employee(4, True)
    E5 = Employee(5, True)

    # Setup relationships:
    E1.reportees = [E2, NE1, E3]
    E2.reportees = [E4]
    NE1.reportees = [E5]

    # Filter the tree to only include engineers using BFS:
    new_root = filter_engineers_bfs(E1)

    # Function to print the tree for verification:
    def print_tree(node, indent=0):
        print(" " * indent + f"{node.employeeId} (Engineer)")
        for child in node.reportees:
            print_tree(child, indent + 4)

    print("Filtered Engineer Tree (BFS):")
    print_tree(new_root)
