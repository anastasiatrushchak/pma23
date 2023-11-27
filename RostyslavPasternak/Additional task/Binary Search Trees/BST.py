# import matplotlib.pyplot as plt
# import networkx as nx
import networkx as nx
from matplotlib import pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout


class BSTNode:
    """A node class for binary search trees. Contains a value, a
    reference to the parent node, and references to two child nodes.
    """
    def __init__(self, data):
        """Construct a new node and set the value attribute. The other
        attributes will be set when the node is added to a tree.
        """
        self.value = data
        self.prev = None
        self.left = None
        self.right = None

class BST:
    """Binary search tree data structure class.
    The root attribute references the first node in the tree.
    """
    def __init__(self):
        """Initialize the root attribute."""
        self.root = None
    # ...
    def find(self, data):
        """Return the node containing the data. If there is no such node
        in the tree, including if the tree is empty, raise a ValueError.
        """
        def _step(current):
            """Recursively step through the tree until the node containing
            the data is found. If there is no such node, raise a Value Error.
            """
            if current is None:
                raise ValueError(str(data) + " is not in the tree.")
            if data == current.value:
                return current
            if data < current.value:
                return _step(current.left)
            else:
                return _step(current.right)


    def insert(self, data):
        def _find_and_link(parent, new_node):
            if new_node.value == parent.value:
                raise ValueError("Duplicate values are not allowed in the tree.")
            elif new_node.value < parent.value:
                if parent.left is None:
                    parent.left = new_node
                    new_node.prev = parent
                else:
                    _find_and_link(parent.left, new_node)
            else:
                if parent.right is None:
                    parent.right = new_node
                    new_node.prev = parent
                else:
                    _find_and_link(parent.right, new_node)

        new_node = BSTNode(data)

        if self.root is None:
            self.root = new_node
        else:
            _find_and_link(self.root, new_node)

    def __str__(self):
        if self.root is None:
            return "[]"
        out, current_level = [], [self.root]
        while current_level:
            next_level, values = [], []
            for node in current_level:
                values.append(node.value)
                for child in [node.left, node.right]:
                    if child is not None:
                        next_level.append(child)
            out.append(values)
            current_level = next_level
        return "\n".join([str(x) for x in out])

    def draw(self):
        """Draw the binary search tree."""
        G = nx.Graph()
        self._add_nodes_edges(G, self.root)
        pos = self._position_nodes(G, self.root, x=0, level=1, pos={}, width=2.0)
        labels = {node: node.value for node in G.nodes()}

        nx.draw(G, pos, labels=labels, with_labels=True, node_size=700, node_color="skyblue", font_size=8, font_color="black", font_weight="bold")
        plt.show()

    def _add_nodes_edges(self, G, node):
        if node:
            G.add_node(node)
            if node.left:
                G.add_edge(node, node.left)
                self._add_nodes_edges(G, node.left)
            if node.right:
                G.add_edge(node, node.right)
                self._add_nodes_edges(G, node.right)

    def _position_nodes(self, G, node, x=0, level=1, pos={}, width=2.0):
        if node:
            pos[node] = ((2 ** (level - 1)) * width) + x, -level
            self._position_nodes(G, node.left, x - width / 2, level + 1, pos, width=width / 2)
            self._position_nodes(G, node.right, x + width / 2, level + 1, pos, width=width / 2)
        return pos

    def remove(self, data):
        if self.root is None:
            raise ValueError("Tree is empty.")
        self.root = self._remove_node(self.root, data)

    def _remove_node(self, current, data):
        if current is None:
            raise ValueError(str(data) + " is not in the tree.")

        if data < current.value:
            current.left = self._remove_node(current.left, data)
        elif data > current.value:
            current.right = self._remove_node(current.right, data)
        else:
            if current.left is None and current.right is None:
                current = None
            elif current.left is None:
                current = current.right
            elif current.right is None:
                current = current.left
            else:
                predecessor = self._find_max(current.left)
                current.value = predecessor.value
                current.left = self._remove_node(current.left, predecessor.value)

        return current

    def _find_max(self, node):
        while node.right:
            node = node.right
        return node