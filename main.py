import random
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
#Пример использования:
root = None
for key in [10, 20, 5, 15]:
    root = insert(root, Node(key))

print(search(root, 15))
root = delete(root, 10)
print(search(root, 10)) 
