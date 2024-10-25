class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # "operator" or "operand"
        self.left = left       # Left child (Node)
        self.right = right     # Right child (Node)
        self.value = value     # Value for operand (attribute, operator, comparison)

    def __repr__(self):
        return f"Node(type={self.type}, value={self.value})"
