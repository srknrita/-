import random
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, priority=None):
        self.key = key
        self.priority = priority if priority else random.randint(1, 1000000)
        self.left = None
        self.right = None

def split(root, key):
    if not root:
        return (None, None)
    if key < root.key:
        left, root.left = split(root.left, key)
        return (left, root)
    else:
        root.right, right = split(root.right, key)
        return (root, right)

def merge(left, right):
    if not left or not right:
        return left or right
    if left.priority > right.priority:
        left.right = merge(left.right, right)
        return left
    else:
        right.left = merge(left, right.left)
        return right

def insert(root, node):
    if not root:
        return node
    if node.priority > root.priority:
        left, right = split(root, node.key)
        node.left, node.right = left, right
        return node
    elif node.key < root.key:
        root.left = insert(root.left, node)
    else:
        root.right = insert(root.right, node)
    return root

def delete(root, key):
    if not root:
        return None
    if root.key == key:
        return merge(root.left, root.right)
    elif key < root.key:
        root.left = delete(root.left, key)
    else:
        root.right = delete(root.right, key)
    return root

def search(root, key):
    if not root:
        return False
    if root.key == key:
        return True
    elif key < root.key:
        return search(root.left, key)
    else:
        return search(root.right, key)

def visualize_treap(root):
    graph = nx.DiGraph()
    pos = {}
    
    def add_edges(node, x=0, y=0, layer=1):
        if node is not None:
            pos[f"{node.key}({node.priority})"] = (x, y)
            if node.left:
                graph.add_edge(f"{node.key}({node.priority})", f"{node.left.key}({node.left.priority})")
                add_edges(node.left, x - 1 / layer, y - 1, layer * 2)
            if node.right:
                graph.add_edge(f"{node.key}({node.priority})", f"{node.right.key}({node.right.priority})")
                add_edges(node.right, x + 1 / layer, y - 1, layer * 2)
    
    if root:
        add_edges(root)
        plt.figure(figsize=(10, 7))
        nx.draw(graph, pos, with_labels=True, node_size=3000, node_color="skyblue", 
                font_size=10, font_weight="bold", arrowsize=20)
        plt.title("Treap Visualization")
        plt.show()

# Пример
root = None
for key in [10, 20, 5, 15]:
    root = insert(root, Node(key))

print("Поиск 15:", search(root, 15))
print("Поиск 10 до удаления:", search(root, 10))

# Визуализация до удаления
print("\nВизуализация Treap до удаления:")
visualize_treap(root)

# Удаление узла
root = delete(root, 10)
print("\nПоиск 10 после удаления:", search(root, 10))

# Визуализация после удаления
print("\nВизуализация Treap после удаления:")
visualize_treap(root)